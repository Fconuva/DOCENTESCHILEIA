"""Regresiones de falsos aprobados, rutas, versiones e instalación no destructiva."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "herramientas"))
from instalar_skill import ROOT_DIRS, instalar
from pipeline_docente import hash_archivo, validar_registro
from validar_material_docente import auditar_guia_html
from validar_repositorio import validar


class ArchivosTemporales(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, text):
        path = self.base / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path


class Material(ArchivosTemporales):
    def html(self, texto):
        return auditar_guia_html(self.write("guia.html", texto))

    def test_e_en_instruccion_no_es_alternativa(self):
        out = self.html('<p>E) Explica la decisión.</p>')
        self.assertFalse(out["errores"])
        self.assertEqual(out["estadisticas"]["reactivos_marcados"], 0)

    def test_ausencia_e_no_prueba_cuatro_opciones(self):
        out = self.html('<p>Pregunta sin opciones.</p>')
        self.assertTrue(any("Sin reactivos" in x for x in out["no_verificado"]))

    def test_opciones_se_cuentan_por_pregunta(self):
        out = self.html('<section data-reactivo="1" data-opciones="4"><p data-opcion="A">Una</p><p data-opcion="B">Dos</p><p data-opcion="C">Tres</p></section>')
        self.assertTrue(out["errores"])

    def test_opcion_duplicada_bloquea(self):
        out = self.html('<section data-reactivo="1" data-opciones="2"><p data-opcion="A">Uno</p><p data-opcion="A">Otro</p></section>')
        self.assertTrue(out["errores"])

    def test_perfil_cinco_opciones_no_se_prohibe_globalmente(self):
        out = self.html('<section data-reactivo="1" data-opciones="5">' + ''.join(f'<p data-opcion="{x}">{x}</p>' for x in 'ABCDE') + '</section>')
        self.assertFalse(out["errores"])

    def test_letter_no_es_a4(self):
        out = self.html('<style>@page {size: Letter;}</style><p>Guía</p>')
        self.assertFalse(any("declara tamaño A4" in x for x in out["comprobaciones"]))

    def test_comentario_css_no_prueba_a4(self):
        out = self.html('<style>/* @page {size:A4} */</style><p>Guía</p>')
        self.assertTrue(out["advertencias"])

    def test_css_renglones_sin_elementos_no_prueba_espacio(self):
        out = self.html('<style>.ln {height: 7mm}</style><p>Escribe.</p>')
        self.assertTrue(any("No se detectaron elementos" in x for x in out["no_verificado"]))

    def test_script_y_cuerpo_vacio_no_aprueban(self):
        out = self.html('<script>Analizar mediante una guía; Nombre Curso</script>')
        self.assertTrue(out["errores"])

    def test_imagen_ausente_bloquea(self):
        self.assertTrue(self.html('<p>Guía</p><img src="ausente.png">')["errores"])

    def test_error_lectura_es_error(self):
        self.assertTrue(auditar_guia_html(self.base / "no-existe.html")["errores"])

    def test_clave_presente_advertida_sin_certificar(self):
        out = self.html('<section data-reactivo="1" data-opciones="2" data-clave="B"><p data-opcion="A">Uno</p><p data-opcion="B">Dos</p></section>')
        self.assertTrue(any("contiene clave" in x for x in out["advertencias"]))
        self.assertEqual(out["estado"], "COMPROBACION_TECNICA_PARCIAL")

    def test_anidamiento_incompleto_bloquea(self):
        self.assertTrue(self.html('<section data-reactivo="1" data-opciones="2"><p>Pregunta')["errores"])

    def test_modelo_editable_no_se_declara_material_final(self):
        out = self.html('<body data-plantilla="modelo"><p>Texto de ejemplo</p></body>')
        self.assertTrue(any("Modelo editable" in x for x in out["advertencias"]))


class Pipeline(ArchivosTemporales):
    def setUp(self):
        super().setUp()
        path = self.write("evidencia.md", "Evidencia sintética para pruebas; no dictamen real.")
        self.ref = {"ruta": path.name, "sha256": hash_archivo(path)}
        self.registro = {"version": 1, "encargo": "Caso sintético", "alcance": "Prueba técnica", "fuentes": [self.ref], "artefactos": [dict(self.ref, destinatario="docente")], "criterios": [{"id": "c1", "resultado": "cumple", "fuente": "fuente sintética", "ubicacion": "archivo completo", "razon": "solo prueba", "evidencia": self.ref}], "roles": {"planeador": "P", "constructor": "C", "verificador": "V", "evaluador": "E"}, "revisiones": [{"rol": role, "identidad": ident, "estado": "completa", "evidencia": self.ref} for role, ident in [("verificador", "V"), ("evaluador", "E")]]}

    def run_case(self):
        return validar_registro(self.write("control.json", json.dumps(self.registro)))

    def test_registro_integro_solo_certifica_estructura(self):
        out = self.run_case()
        self.assertFalse(out["errores"])
        self.assertEqual(out["estado"], "REGISTRO_TECNICO_COMPLETO_NO_CERTIFICA_PEDAGOGIA")

    def test_hash_desactualizado_bloquea(self):
        self.write("evidencia.md", "Cambió la versión")
        self.assertTrue(self.run_case()["errores"])

    def test_listas_vacias_no_aprueban(self):
        for field in ("fuentes", "artefactos", "criterios", "revisiones"):
            with self.subTest(field=field):
                original = self.registro[field]
                self.registro[field] = []
                self.assertTrue(self.run_case()["errores"])
                self.registro[field] = original

    def test_constructor_no_puede_verificarse_independientemente(self):
        self.registro["roles"]["verificador"] = "C"
        self.assertTrue(self.run_case()["errores"])

    def test_identidad_no_se_diferencia_solo_por_mayusculas(self):
        self.registro["roles"]["verificador"] = " c "
        self.assertTrue(self.run_case()["errores"])

    def test_ruta_fuera_del_encargo_bloquea(self):
        self.registro["fuentes"] = [{"ruta": "../fuera.md", "sha256": "0" * 64}]
        self.assertTrue(self.run_case()["errores"])

    def test_no_aplica_exige_razon_y_evidencia(self):
        self.registro["criterios"][0].update(resultado="no_aplica", razon="")
        self.assertTrue(self.run_case()["errores"])

    def test_revision_pendiente_bloquea(self):
        self.registro["revisiones"][0]["estado"] = "pendiente"
        self.assertTrue(self.run_case()["errores"])

    def test_json_malformado(self):
        self.assertTrue(validar_registro(self.write("roto.json", "{"))["errores"])

    def test_tipos_erroneos_no_abren_puerta(self):
        for field, value in [("version", True), ("criterios", [None]), ("roles", []), ("fuentes", [42]), ("revisiones", [None])]:
            with self.subTest(field=field):
                original = copy.deepcopy(self.registro)
                self.registro[field] = value
                self.assertTrue(self.run_case()["errores"])
                self.registro = original

    def test_tipos_erroneos_en_campos_anidados_se_reportan(self):
        self.registro["criterios"][0]["resultado"] = []
        self.registro["revisiones"][0]["rol"] = {}
        self.assertTrue(self.run_case()["errores"])


class Instalacion(ArchivosTemporales):
    def setUp(self):
        super().setUp()
        self.source = self.base / "source"
        self.dest = self.base / "profile" / "docentes-chile-ia"
        self.write("source/SKILL.md", "Skill de prueba")
        self.write("source/conocimiento/ref.md", "Referencia")
        self.write("source/secreto.local.json", "No copiar")
        self.write("source/herramientas/privado.local.json", "No copiar")
        self.write("source/.git/config", "No copiar")

    def test_simulacion_no_escribe(self):
        report = instalar(self.source, self.dest)
        self.assertEqual(report["modo"], "simulacion")
        self.assertFalse(self.dest.parent.exists())

    def test_copia_referencias_y_excluye_privados_y_git(self):
        instalar(self.source, self.dest, True)
        self.assertTrue((self.dest / "conocimiento/ref.md").is_file())
        self.assertFalse((self.dest / ".git").exists())
        self.assertFalse((self.dest / "herramientas/privado.local.json").exists())

    def test_instalacion_existente_se_preserva(self):
        self.dest.mkdir(parents=True)
        (self.dest / "SKILL.md").write_text("Conservar", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            instalar(self.source, self.dest, True)
        self.assertEqual((self.dest / "SKILL.md").read_text(encoding="utf-8"), "Conservar")

    def test_destino_dentro_del_origen_bloquea(self):
        with self.assertRaises(ValueError):
            instalar(self.source, self.source / "nested", True)


class Estructura(ArchivosTemporales):
    def skill(self):
        self.write("SKILL.md", "---\nname: prueba-docente\ndescription: Prueba con propósito delimitado.\n---\n[Referencia](referencia.md)\n")

    def test_enlace_roto_es_error(self):
        self.skill()
        self.assertTrue(validar(self.base)["errores"])

    def test_referencias_presentes_son_resueltas(self):
        self.skill()
        self.write("referencia.md", "Contenido propio")
        self.assertFalse(validar(self.base)["errores"])

    def test_sin_frontmatter_no_es_skill_valida(self):
        self.write("SKILL.md", "Solo una cabecera")
        self.assertTrue(validar(self.base)["errores"])


class PaqueteParaDocentes(unittest.TestCase):
    """El paquete se abre como carpeta en Antigravity: las skills deben estar donde las busca."""

    raiz = Path(__file__).resolve().parents[1]
    skills_docente = {"empezar", "planificar-clase", "planificar-unidad", "planificar-anual", "crear-evaluacion", "revisar-material"}

    def test_skills_en_la_ruta_estandar(self):
        nombres = {p.parent.name for p in (self.raiz / ".agents" / "skills").glob("*/SKILL.md")}
        self.assertTrue(self.skills_docente <= nombres, self.skills_docente - nombres)

    def test_no_quedan_rutas_que_antigravity_no_lee(self):
        self.assertFalse((self.raiz / ".github" / "skills").exists())
        self.assertFalse((self.raiz / ".agent").exists())

    def test_nombre_de_skill_coincide_con_su_carpeta(self):
        for ruta in (self.raiz / ".agents" / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=ruta.parent.name):
                cabecera = ruta.read_text(encoding="utf-8").split("---")[1]
                self.assertIn(f"name: {ruta.parent.name}\n", cabecera)

    def test_reglas_comunes_caben_en_el_limite_de_antigravity(self):
        self.assertLess((self.raiz / "AGENTS.md").stat().st_size, 24000)

    def test_cada_pdf_oficial_tiene_texto_buscable(self):
        for carpeta in ("marco_curricular/documentos_oficiales", "temarios_evaluacion_docente_2026"):
            for pdf in (self.raiz / carpeta).glob("*.pdf"):
                with self.subTest(pdf=pdf.name):
                    txt = pdf.with_suffix(".txt")
                    self.assertTrue(txt.is_file())
                    self.assertIn("[página 1 del PDF]", txt.read_text(encoding="utf-8")[:2000])

    def test_modelos_de_planificacion_declaran_a4_y_objetivo(self):
        for nombre in ("Planificacion_Anual_Modelo", "Planificacion_Unidad_Modelo", "Planificacion_Clase_3_Momentos_Modelo"):
            with self.subTest(modelo=nombre):
                out = auditar_guia_html(self.raiz / "documentos_modelo" / "planificaciones" / f"{nombre}.html")
                self.assertFalse(out["errores"])
                self.assertTrue(any("tamaño A4" in x for x in out["comprobaciones"]))
                self.assertTrue(any("data-objetivo" in x for x in out["comprobaciones"]))

    def test_indice_de_oa_apunta_a_listas_de_objetivos(self):
        indice = (self.raiz / "marco_curricular" / "INDICE_DE_OA.md").read_text(encoding="utf-8")
        archivo, lineas, filas = None, [], 0
        for renglon in indice.split("\n"):
            if renglon.startswith("Archivo: `"):
                archivo = renglon.split("`")[1]
                lineas = (self.raiz / archivo).read_text(encoding="utf-8").split("\n")
            celdas = [c.strip() for c in renglon.split("|")]
            if archivo and len(celdas) == 6 and celdas[4].isdigit():
                filas += 1
                inicio = int(celdas[4]) - 1
                tramo = "\n".join(lineas[inicio:inicio + 30])
                with self.subTest(archivo=archivo, linea=celdas[4]):
                    self.assertIn("Objetivos de Aprendizaje", tramo)
                    self.assertIn(f"[página {celdas[3]} del PDF]", "\n".join(lineas[max(inicio - 60, 0):inicio + 1]))
        self.assertGreater(filas, 100)

    def test_carpeta_del_docente_no_se_instala(self):
        self.assertNotIn("mi_trabajo", ROOT_DIRS)


if __name__ == "__main__":
    unittest.main()
