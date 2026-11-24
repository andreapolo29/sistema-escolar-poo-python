import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
from modelos import Colegio, Estudiante, Profesor, Solicitud, Traslado

ARCHIVO_DATOS = "datos_colegios.json"


class AppSistemaEscolar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Escolar - POO")
        self.root.geometry("760x560")

        self.colegios = []
        self.estudiantes = []
        self.profesores = []
        self.traslados = []
        self.solicitudes = []

        self.cargar_datos()
        self.crear_interfaz()
        self.actualizar_listas()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.root,
            text="Sistema Educativo Interinstitucional (POO)",
            font=("Arial", 14, "bold"),
            pady=10,
        )
        titulo.pack()

        self.pestanas = ttk.Notebook(self.root)
        self.pestanas.pack(fill="both", expand=True, padx=10, pady=5)

        self.tab_colegios = tk.Frame(self.pestanas)
        self.tab_estudiantes = tk.Frame(self.pestanas)
        self.tab_traslados = tk.Frame(self.pestanas)
        self.tab_solicitudes = tk.Frame(self.pestanas)

        self.pestanas.add(self.tab_colegios, text="Colegios y Profesores")
        self.pestanas.add(self.tab_estudiantes, text="Estudiantes")
        self.pestanas.add(self.tab_traslados, text="Traslados")
        self.pestanas.add(self.tab_solicitudes, text="Solicitudes")

        self.armar_tab_colegios()
        self.armar_tab_estudiantes()
        self.armar_tab_traslados()
        self.armar_tab_solicitudes()

    # ---------------- COLEGIOS Y PROFESORES ----------------
    def armar_tab_colegios(self):
        marco = tk.LabelFrame(self.tab_colegios, text="Registrar Colegio", padx=10, pady=10)
        marco.pack(fill="x", padx=10, pady=8)

        tk.Label(marco, text="Nombre del colegio:").grid(row=0, column=0, sticky="w")
        self.entry_col_nombre = tk.Entry(marco, width=30)
        self.entry_col_nombre.grid(row=0, column=1, padx=5)

        tk.Label(marco, text="Ciudad:").grid(row=0, column=2, sticky="w")
        self.entry_col_ciudad = tk.Entry(marco, width=20)
        self.entry_col_ciudad.grid(row=0, column=3, padx=5)

        tk.Button(marco, text="Guardar Colegio", command=self.agregar_colegio).grid(
            row=0, column=4, padx=10
        )

        marco_prof = tk.LabelFrame(
            self.tab_colegios, text="Registrar Profesor", padx=10, pady=10
        )
        marco_prof.pack(fill="x", padx=10, pady=8)

        tk.Label(marco_prof, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_prof_nombre = tk.Entry(marco_prof, width=20)
        self.entry_prof_nombre.grid(row=0, column=1, padx=5)

        tk.Label(marco_prof, text="Documento:").grid(row=0, column=2, sticky="w")
        self.entry_prof_doc = tk.Entry(marco_prof, width=15)
        self.entry_prof_doc.grid(row=0, column=3, padx=5)

        tk.Label(marco_prof, text="Materia:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_prof_mat = tk.Entry(marco_prof, width=20)
        self.entry_prof_mat.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(marco_prof, text="Correo:").grid(row=1, column=2, sticky="w", pady=5)
        self.entry_prof_correo = tk.Entry(marco_prof, width=20)
        self.entry_prof_correo.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(marco_prof, text="Guardar Profesor", command=self.agregar_profesor).grid(
            row=1, column=4, padx=10
        )

        self.lista_colegios = tk.Listbox(self.tab_colegios, height=12)
        self.lista_colegios.pack(fill="both", expand=True, padx=10, pady=8)

    def agregar_colegio(self):
        nombre = self.entry_col_nombre.get().strip()
        ciudad = self.entry_col_ciudad.get().strip()
        if not nombre or not ciudad:
            messagebox.showwarning("Aviso", "Escribe el nombre del colegio y la ciudad.")
            return

        nuevo = Colegio(nombre, ciudad)
        self.colegios.append(nuevo)
        self.entry_col_nombre.delete(0, tk.END)
        self.entry_col_ciudad.delete(0, tk.END)
        self.guardar_datos()
        self.actualizar_listas()

    def agregar_profesor(self):
        nombre = self.entry_prof_nombre.get().strip()
        doc = self.entry_prof_doc.get().strip()
        materia = self.entry_prof_mat.get().strip()
        correo = self.entry_prof_correo.get().strip() or "sin_correo@colegio.edu.co"
        if not nombre or not doc or not materia:
            messagebox.showwarning("Aviso", "Completa nombre, documento y materia.")
            return

        prof = Profesor(nombre, doc, correo, materia)
        self.profesores.append(prof)
        self.entry_prof_nombre.delete(0, tk.END)
        self.entry_prof_doc.delete(0, tk.END)
        self.entry_prof_mat.delete(0, tk.END)
        self.entry_prof_correo.delete(0, tk.END)
        self.guardar_datos()
        self.actualizar_listas()

    # ---------------- ESTUDIANTES ----------------
    def armar_tab_estudiantes(self):
        marco = tk.LabelFrame(
            self.tab_estudiantes, text="Registrar Estudiante", padx=10, pady=10
        )
        marco.pack(fill="x", padx=10, pady=8)

        tk.Label(marco, text="Nombre:").grid(row=0, column=0, sticky="w")
        self.entry_est_nombre = tk.Entry(marco, width=22)
        self.entry_est_nombre.grid(row=0, column=1, padx=5)

        tk.Label(marco, text="Documento:").grid(row=0, column=2, sticky="w")
        self.entry_est_doc = tk.Entry(marco, width=18)
        self.entry_est_doc.grid(row=0, column=3, padx=5)

        tk.Label(marco, text="Grado:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_est_grado = tk.Entry(marco, width=22)
        self.entry_est_grado.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(marco, text="Colegio actual:").grid(row=1, column=2, sticky="w", pady=5)
        self.entry_est_colegio = tk.Entry(marco, width=25)
        self.entry_est_colegio.grid(row=1, column=3, padx=5, pady=5)

        tk.Button(marco, text="Guardar Estudiante", command=self.agregar_estudiante).grid(
            row=1, column=4, padx=10
        )

        self.lista_estudiantes = tk.Listbox(self.tab_estudiantes, height=14)
        self.lista_estudiantes.pack(fill="both", expand=True, padx=10, pady=8)

    def agregar_estudiante(self):
        nombre = self.entry_est_nombre.get().strip()
        doc = self.entry_est_doc.get().strip()
        grado = self.entry_est_grado.get().strip()
        colegio = self.entry_est_colegio.get().strip()
        if not nombre or not doc or not grado or not colegio:
            messagebox.showwarning("Aviso", "Completa todos los campos del estudiante.")
            return

        est = Estudiante(nombre, doc, f"{doc}@estudiante.edu.co", grado, colegio)
        self.estudiantes.append(est)
        self.entry_est_nombre.delete(0, tk.END)
        self.entry_est_doc.delete(0, tk.END)
        self.entry_est_grado.delete(0, tk.END)
        self.entry_est_colegio.delete(0, tk.END)
        self.guardar_datos()
        self.actualizar_listas()

    # ---------------- TRASLADOS ----------------
    def armar_tab_traslados(self):
        marco = tk.LabelFrame(
            self.tab_traslados, text="Solicitar Traslado de Colegio", padx=10, pady=10
        )
        marco.pack(fill="x", padx=10, pady=8)

        tk.Label(marco, text="Estudiante:").grid(row=0, column=0, sticky="w")
        self.combo_est_traslado = ttk.Combobox(marco, width=26, state="readonly")
        self.combo_est_traslado.grid(row=0, column=1, padx=5)

        tk.Label(marco, text="Colegio destino:").grid(row=0, column=2, sticky="w")
        self.entry_col_destino = tk.Entry(marco, width=26)
        self.entry_col_destino.grid(row=0, column=3, padx=5)

        tk.Label(marco, text="Motivo:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_motivo_traslado = tk.Entry(marco, width=55)
        self.entry_motivo_traslado.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        tk.Button(marco, text="Registrar Traslado", command=self.crear_traslado).grid(
            row=1, column=4, padx=10
        )

        self.lista_traslados = tk.Listbox(self.tab_traslados, height=11)
        self.lista_traslados.pack(fill="both", expand=True, padx=10, pady=5)

        botones = tk.Frame(self.tab_traslados)
        botones.pack(pady=5)
        tk.Button(botones, text="Aprobar Traslado", command=self.aprobar_traslado).pack(
            side="left", padx=5
        )
        tk.Button(botones, text="Rechazar Traslado", command=self.rechazar_traslado).pack(
            side="left", padx=5
        )

    def crear_traslado(self):
        idx = self.combo_est_traslado.current()
        destino = self.entry_col_destino.get().strip()
        motivo = self.entry_motivo_traslado.get().strip() or "Cambio de domicilio / colegio"

        if idx < 0 or not destino:
            messagebox.showwarning("Aviso", "Selecciona un estudiante y escribe el colegio destino.")
            return

        est = self.estudiantes[idx]
        origen = est.get_colegio_actual()
        traslado = Traslado(est, origen, destino, motivo)
        self.traslados.append(traslado)

        self.entry_col_destino.delete(0, tk.END)
        self.entry_motivo_traslado.delete(0, tk.END)
        self.guardar_datos()
        self.actualizar_listas()

    def aprobar_traslado(self):
        sel = self.lista_traslados.curselection()
        if not sel:
            messagebox.showinfo("Info", "Selecciona un traslado de la lista.")
            return
        traslado = self.traslados[sel[0]]
        traslado.aprobar()
        self.guardar_datos()
        self.actualizar_listas()

    def rechazar_traslado(self):
        sel = self.lista_traslados.curselection()
        if not sel:
            messagebox.showinfo("Info", "Selecciona un traslado de la lista.")
            return
        traslado = self.traslados[sel[0]]
        traslado.rechazar()
        self.guardar_datos()
        self.actualizar_listas()

    # ---------------- SOLICITUDES ----------------
    def armar_tab_solicitudes(self):
        marco = tk.LabelFrame(
            self.tab_solicitudes, text="Nueva Solicitud", padx=10, pady=10
        )
        marco.pack(fill="x", padx=10, pady=8)

        tk.Label(marco, text="Solicitante:").grid(row=0, column=0, sticky="w")
        self.entry_sol_persona = tk.Entry(marco, width=22)
        self.entry_sol_persona.grid(row=0, column=1, padx=5)

        tk.Label(marco, text="Tipo:").grid(row=0, column=2, sticky="w")
        self.entry_sol_tipo = tk.Entry(marco, width=22)
        self.entry_sol_tipo.grid(row=0, column=3, padx=5)

        tk.Label(marco, text="Descripcion:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_sol_desc = tk.Entry(marco, width=52)
        self.entry_sol_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        tk.Button(marco, text="Enviar Solicitud", command=self.crear_solicitud).grid(
            row=1, column=4, padx=10
        )

        self.lista_solicitudes = tk.Listbox(self.tab_solicitudes, height=11)
        self.lista_solicitudes.pack(fill="both", expand=True, padx=10, pady=5)

        botones = tk.Frame(self.tab_solicitudes)
        botones.pack(pady=5)
        tk.Button(botones, text="Marcar Aprobada", command=self.aprobar_solicitud).pack(
            side="left", padx=5
        )
        tk.Button(botones, text="Marcar Rechazada", command=self.rechazar_solicitud).pack(
            side="left", padx=5
        )

    def crear_solicitud(self):
        nombre_pers = self.entry_sol_persona.get().strip()
        tipo = self.entry_sol_tipo.get().strip()
        desc = self.entry_sol_desc.get().strip()
        if not nombre_pers or not tipo or not desc:
            messagebox.showwarning("Aviso", "Completa solicitante, tipo y descripcion.")
            return

        persona_obj = Estudiante(nombre_pers, "N/A", "N/A", "N/A", "N/A")
        sol = Solicitud(persona_obj, tipo, desc)
        self.solicitudes.append(sol)

        self.entry_sol_persona.delete(0, tk.END)
        self.entry_sol_tipo.delete(0, tk.END)
        self.entry_sol_desc.delete(0, tk.END)
        self.guardar_datos()
        self.actualizar_listas()

    def aprobar_solicitud(self):
        sel = self.lista_solicitudes.curselection()
        if not sel:
            return
        self.solicitudes[sel[0]].cambiar_estado("Aprobada")
        self.guardar_datos()
        self.actualizar_listas()

    def rechazar_solicitud(self):
        sel = self.lista_solicitudes.curselection()
        if not sel:
            return
        self.solicitudes[sel[0]].cambiar_estado("Rechazada")
        self.guardar_datos()
        self.actualizar_listas()

    # ---------------- ACTUALIZAR Y GUARDAR ----------------
    def actualizar_listas(self):
        self.lista_colegios.delete(0, tk.END)
        for c in self.colegios:
            self.lista_colegios.insert(tk.END, c.mostrar_info())
        for p in self.profesores:
            self.lista_colegios.insert(tk.END, p.mostrar_info())

        self.lista_estudiantes.delete(0, tk.END)
        opciones_est = []
        for e in self.estudiantes:
            self.lista_estudiantes.insert(tk.END, e.mostrar_info())
            opciones_est.append(f"{e.get_nombre()} ({e.get_colegio_actual()})")
        self.combo_est_traslado["values"] = opciones_est

        self.lista_traslados.delete(0, tk.END)
        for t in self.traslados:
            self.lista_traslados.insert(tk.END, t.mostrar_info())

        self.lista_solicitudes.delete(0, tk.END)
        for s in self.solicitudes:
            self.lista_solicitudes.insert(tk.END, s.mostrar_info())

    def guardar_datos(self):
        data = {
            "colegios": [
                {"nombre": c.get_nombre(), "ciudad": c.get_ciudad()} for c in self.colegios
            ],
            "profesores": [
                {
                    "nombre": p.get_nombre(),
                    "documento": p.get_documento(),
                    "correo": p.get_correo(),
                    "materia": p.get_materia(),
                }
                for p in self.profesores
            ],
            "estudiantes": [
                {
                    "nombre": e.get_nombre(),
                    "documento": e.get_documento(),
                    "correo": e.get_correo(),
                    "grado": e.get_grado(),
                    "colegio_actual": e.get_colegio_actual(),
                    "estado": e.get_estado(),
                }
                for e in self.estudiantes
            ],
            "traslados": [
                {
                    "estudiante_nombre": t.get_estudiante().get_nombre(),
                    "estudiante_doc": t.get_estudiante().get_documento(),
                    "colegio_origen": t.get_colegio_origen(),
                    "colegio_destino": t.get_colegio_destino(),
                    "motivo": t.get_motivo(),
                    "estado": t.get_estado(),
                }
                for t in self.traslados
            ],
            "solicitudes": [
                {
                    "persona": s.get_persona().get_nombre(),
                    "tipo": s.get_tipo(),
                    "descripcion": s.get_descripcion(),
                    "estado": s.get_estado(),
                }
                for s in self.solicitudes
            ],
        }
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        if not os.path.exists(ARCHIVO_DATOS):
            self.colegios = []
            self.estudiantes = []
            self.profesores = []
            self.traslados = []
            self.solicitudes = []
            self.guardar_datos()
            return

        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.colegios = [
            Colegio(item["nombre"], item["ciudad"]) for item in data.get("colegios", [])
        ]
        self.profesores = [
            Profesor(
                item["nombre"], item["documento"], item["correo"], item["materia"]
            )
            for item in data.get("profesores", [])
        ]
        self.estudiantes = []
        for item in data.get("estudiantes", []):
            est = Estudiante(
                item["nombre"],
                item["documento"],
                item["correo"],
                item["grado"],
                item["colegio_actual"],
            )
            est.set_estado(item.get("estado", "Activo"))
            self.estudiantes.append(est)

        self.traslados = []
        for item in data.get("traslados", []):
            est_encontrado = next(
                (e for e in self.estudiantes if e.get_documento() == item["estudiante_doc"]),
                Estudiante(
                    item["estudiante_nombre"],
                    item["estudiante_doc"],
                    "N/A",
                    "N/A",
                    item["colegio_origen"],
                ),
            )
            tr = Traslado(
                est_encontrado,
                item["colegio_origen"],
                item["colegio_destino"],
                item["motivo"],
            )
            if item.get("estado") == "Aprobado":
                tr.aprobar()
            elif item.get("estado") == "Rechazado":
                tr.rechazar()
            self.traslados.append(tr)

        self.solicitudes = []
        for item in data.get("solicitudes", []):
            per = Estudiante(item["persona"], "N/A", "N/A", "N/A", "N/A")
            sol = Solicitud(per, item["tipo"], item["descripcion"])
            sol.cambiar_estado(item.get("estado", "Pendiente"))
            self.solicitudes.append(sol)


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppSistemaEscolar(ventana)
    ventana.mainloop()