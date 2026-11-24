from datetime import date


class Persona:
    def __init__(self, nombre: str, documento: str = "N/A", correo: str = "sin_correo@colegio.edu.co", telefono: str = ""):
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono
        self.__sesion_activa = False

    def get_nombre(self) -> str:
        return self.__nombre

    def get_documento(self) -> str:
        return self.__documento

    def get_correo(self) -> str:
        return self.__correo

    def get_telefono(self) -> str:
        return self.__telefono

    def iniciar_sesion(self, correo: str, clave: str) -> bool:
        self.__sesion_activa = bool(correo.strip() and clave.strip())
        return self.__sesion_activa

    def actualizar_datos(self, telefono: str, correo: str) -> None:
        if telefono.strip():
            self.__telefono = telefono.strip()
        if correo.strip():
            self.__correo = correo.strip()

    def consultar_informacion(self) -> dict:
        return {
            "nombre": self.__nombre,
            "documento": self.__documento,
            "correo": self.__correo,
            "telefono": self.__telefono,
            "sesion_activa": self.__sesion_activa,
        }


class Estudiante(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, grado: str, colegio_actual: str, estado: str = "Activo"):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__grado = str(grado)
        self.__colegio_actual = colegio_actual
        self.__estado = estado
        self.__fecha_ingreso = date.today().isoformat()
        self.__calificaciones: list[dict] = []
        self.__horarios: list[dict] = []

    def get_grado(self) -> str:
        return self.__grado

    def get_colegio_actual(self) -> str:
        return self.__colegio_actual

    def set_colegio_actual(self, colegio: str) -> None:
        self.__colegio_actual = colegio

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado: str) -> None:
        self.__estado = estado

    def solicitar_traslado(self, destino: str, motivo: str = "Traslado escolar") -> "Traslado":
        return Traslado(self, self.__colegio_actual, destino, motivo)

    def realizar_solicitud(self, tipo: str, descripcion: str) -> "Solicitud":
        return Solicitud(self, tipo, descripcion)

    def consultar_calificaciones(self) -> list[dict]:
        return list(self.__calificaciones)

    def consultar_horarios(self) -> list[dict]:
        return list(self.__horarios)

    def mostrar_info(self) -> str:
        return f"Estudiante: {self.get_nombre()} | Doc: {self.get_documento()} | Grado: {self.__grado} | Colegio: {self.__colegio_actual} | Estado: {self.__estado}"


class Profesor(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, materia: str):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__materia = materia
        self.__fecha_contrato = date.today().isoformat()

    def get_materia(self) -> str:
        return self.__materia

    def asignar_calificacion(self, estudiante: Estudiante, nota: float, observacion: str = "") -> "Calificacion":
        return Calificacion(nota=nota, observacion=observacion)

    def consultar_horarios(self) -> list:
        return []

    def pasar_asistencia(self, curso_id: str, presentes: list[str]) -> dict:
        return {"curso_id": curso_id, "fecha": date.today().isoformat(), "presentes": presentes}

    def mostrar_info(self) -> str:
        return f"Profesor: {self.get_nombre()} | Doc: {self.get_documento()} | Materia: {self.__materia}"


class Rector(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, cargo: str = "Rector"):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__cargo = cargo
        self.__fecha_inicio = date.today().isoformat()

    def aprobar_solicitud(self, solicitud: "Solicitud") -> None:
        solicitud.cambiar_estado("Aprobada")

    def consultar_informe(self, colegio: "Colegio") -> str:
        return colegio.mostrar_info()

    def gestionar_colegio(self, colegio: "Colegio", ciudad: str) -> None:
        colegio.set_ciudad(ciudad)


class Coordinador(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, area: str = "Academica"):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__area = area

    def revisar_solicitud(self, solicitud: "Solicitud", estado: str = "En revision") -> None:
        solicitud.cambiar_estado(estado)

    def aprobar_traslado(self, traslado: "Traslado") -> None:
        traslado.aprobar()

    def asignar_curso(self, estudiante: Estudiante, curso: "Curso") -> bool:
        return curso.agregar_estudiante(estudiante)


class PadreFamilia(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, parentesco: str = "Acudiente", ocupacion: str = ""):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__parentesco = parentesco
        self.__ocupacion = ocupacion

    def consultar_informacion_estudiante(self, estudiante: Estudiante) -> str:
        return estudiante.mostrar_info()

    def realizar_solicitud(self, tipo: str, descripcion: str) -> "Solicitud":
        return Solicitud(self, tipo, descripcion)

    def consultar_calificaciones(self, estudiante: Estudiante) -> list[dict]:
        return estudiante.consultar_calificaciones()


class Secretaria(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, area: str = "Secretaria"):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__area = area

    def registrar_matricula(self, matricula: "Matricula") -> None:
        matricula.registrar()

    def verificar_documentos(self, documento: "Documento") -> bool:
        return documento.verificar()

    def actualizar_informacion(self, telefono: str, correo: str) -> None:
        self.actualizar_datos(telefono, correo)


class Administrativo(Persona):
    def __init__(self, nombre: str, documento: str, correo: str, cargo: str = "Administrativo", area: str = "General"):
        super().__init__(nombre=nombre, documento=documento, correo=correo)
        self.__cargo = cargo
        self.__area = area

    def consultar_solicitud(self, solicitud: "Solicitud") -> str:
        return solicitud.mostrar_info()

    def actualizar_datos_administrativos(self, telefono: str, correo: str) -> None:
        self.actualizar_datos(telefono, correo)


class Colegio:
    def __init__(self, nombre: str, ciudad: str, nit: str = "", direccion: str = "", telefono: str = "", correo: str = ""):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__nit = nit
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__sedes: list["Sede"] = []

    def get_nombre(self) -> str:
        return self.__nombre

    def get_ciudad(self) -> str:
        return self.__ciudad

    def set_ciudad(self, ciudad: str) -> None:
        if ciudad.strip():
            self.__ciudad = ciudad.strip()

    def registrar_sede(self, sede: "Sede") -> None:
        self.__sedes.append(sede)

    def gestionar_estudiante(self, estudiante: Estudiante) -> None:
        estudiante.set_colegio_actual(self.__nombre)

    def consultar_sedes(self) -> list["Sede"]:
        return list(self.__sedes)

    def generar_informe(self) -> str:
        return self.mostrar_info()

    def mostrar_info(self) -> str:
        return f"Colegio: {self.__nombre} | Ciudad: {self.__ciudad}"


class Sede:
    def __init__(self, id_sede: int, nombre: str, capacidad: int, tipo: str = "Principal"):
        self.__id_sede = id_sede
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__tipo = tipo
        self.__disponible = True

    def reservar(self) -> bool:
        if not self.__disponible:
            return False
        self.__disponible = False
        return True

    def liberar(self) -> None:
        self.__disponible = True

    def consultar_disponibilidad(self) -> bool:
        return self.__disponible


class Aula:
    def __init__(self, id_aula: int, nombre: str, capacidad: int, tipo: str = "General"):
        self.__id_aula = id_aula
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__tipo = tipo
        self.__disponible = True

    def reservar(self) -> bool:
        if not self.__disponible:
            return False
        self.__disponible = False
        return True

    def liberar(self) -> None:
        self.__disponible = True

    def consultar_disponibilidad(self) -> bool:
        return self.__disponible


class Curso:
    def __init__(self, id_curso: str, nombre: str, grado: int, jornada: str, capacidad: int):
        self.__id_curso = id_curso
        self.__nombre = nombre
        self.__grado = grado
        self.__jornada = jornada
        self.__capacidad = capacidad
        self.__estudiantes: list[Estudiante] = []
        self.__profesores: list[Profesor] = []

    def agregar_estudiante(self, estudiante: Estudiante) -> bool:
        if len(self.__estudiantes) >= self.__capacidad:
            return False
        self.__estudiantes.append(estudiante)
        return True

    def retirar_estudiante(self, estudiante: Estudiante) -> bool:
        antes = len(self.__estudiantes)
        self.__estudiantes = [e for e in self.__estudiantes if e.get_documento() != estudiante.get_documento()]
        return len(self.__estudiantes) < antes

    def asignar_profesor(self, profesor: Profesor) -> None:
        self.__profesores.append(profesor)

    def consultar_estudiantes(self) -> list[Estudiante]:
        return list(self.__estudiantes)


class Matricula:
    def __init__(self, id_matricula: str, fecha_matricula: str | None = None, estado: str = "Pendiente"):
        self.__id_matricula = id_matricula
        self.__fecha_matricula = fecha_matricula or date.today().isoformat()
        self.__estado = estado

    def registrar(self) -> None:
        self.__estado = "Registrada"

    def cancelar(self) -> None:
        self.__estado = "Cancelada"

    def actualizar_estado(self, estado: str) -> None:
        self.__estado = estado

    def verificar_documentos(self, documentos: list["Documento"]) -> bool:
        return len(documentos) > 0 and all(d.verificar() for d in documentos)


class Pago:
    def __init__(self, id_pago: str, fecha: str | None = None, hora: str = "08:00", estado: str = "Pendiente", monto: float = 0.0):
        self.__id_pago = id_pago
        self.__fecha = fecha or date.today().isoformat()
        self.__hora = hora
        self.__estado = estado
        self.__monto = monto

    def registrar_pago(self, monto: float) -> None:
        self.__monto = monto
        self.__estado = "Pagado"

    def consultar_pago(self) -> dict:
        return {"id_pago": self.__id_pago, "fecha": self.__fecha, "hora": self.__hora, "estado": self.__estado, "monto": self.__monto}

    def actualizar_estado(self, estado: str) -> None:
        self.__estado = estado


class Traslado:
    def __init__(self, estudiante: Estudiante, colegio_origen: str, colegio_destino: str, motivo: str = "", estado: str = "Pendiente"):
        self.__estudiante = estudiante
        self.__colegio_origen = colegio_origen
        self.__colegio_destino = colegio_destino
        self.__motivo = motivo
        self.__fecha_solicitud = date.today().isoformat()
        self.__estado = estado

    def get_estudiante(self) -> Estudiante:
        return self.__estudiante

    def get_colegio_origen(self) -> str:
        return self.__colegio_origen

    def get_colegio_destino(self) -> str:
        return self.__colegio_destino

    def get_motivo(self) -> str:
        return self.__motivo

    def get_estado(self) -> str:
        return self.__estado

    def solicitar(self) -> None:
        self.__estado = "Pendiente"

    def aprobar(self) -> None:
        self.__estado = "Aprobado"
        self.__estudiante.set_colegio_actual(self.__colegio_destino)

    def rechazar(self, motivo: str | None = None) -> None:
        self.__estado = "Rechazado"
        if motivo:
            self.__motivo = motivo

    def consultar_estado(self) -> str:
        return self.__estado

    def mostrar_info(self) -> str:
        return f"Traslado: {self.__estudiante.get_nombre()} | {self.__colegio_origen} -> {self.__colegio_destino} | Estado: {self.__estado}"


class Solicitud:
    def __init__(self, persona: Persona, tipo: str, descripcion: str, estado: str = "Pendiente"):
        self.__persona = persona
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__fecha_solicitud = date.today().isoformat()
        self.__estado = estado

    def get_persona(self) -> Persona:
        return self.__persona

    def get_tipo(self) -> str:
        return self.__tipo

    def get_descripcion(self) -> str:
        return self.__descripcion

    def get_estado(self) -> str:
        return self.__estado

    def crear(self) -> None:
        self.__estado = "Pendiente"

    def cancelar(self) -> None:
        self.__estado = "Cancelada"

    def cambiar_estado(self, estado: str) -> None:
        self.__estado = estado

    def consultar_estado(self) -> str:
        return self.__estado

    def mostrar_info(self) -> str:
        return f"Solicitud [{self.__tipo}] de {self.__persona.get_nombre()}: {self.__descripcion} | Estado: {self.__estado}"


class Documento:
    def __init__(self, nombre: str, tipo: str, fecha_entrega: str | None = None, estado: str = "Pendiente"):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__fecha_entrega = fecha_entrega or date.today().isoformat()
        self.__estado = estado
        self.__cargado = False

    def cargar(self) -> None:
        self.__cargado = True
        self.__estado = "Cargado"

    def verificar(self) -> bool:
        return self.__cargado

    def actualizar_estado(self, estado: str) -> None:
        self.__estado = estado


class Notificacion:
    def __init__(self, mensaje: str, fecha: str | None = None, estado: str = "No leida"):
        self.__mensaje = mensaje
        self.__fecha = fecha or date.today().isoformat()
        self.__estado = estado

    def enviar(self) -> None:
        self.__estado = "Enviada"

    def marcar_leida(self) -> None:
        self.__estado = "Leida"

    def consultar_notificacion(self) -> dict:
        return {"mensaje": self.__mensaje, "fecha": self.__fecha, "estado": self.__estado}


class PeriodoAcademico:
    def __init__(self, nombre: str, fecha_inicio: str, fecha_fin: str, estado: str = "Inactivo"):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__estado = estado

    def iniciar_periodo(self) -> None:
        self.__estado = "Activo"

    def cerrar_periodo(self) -> None:
        self.__estado = "Cerrado"

    def consultar_estado(self) -> str:
        return self.__estado


class Calificacion:
    def __init__(self, nota: float, fecha: str | None = None, observacion: str = ""):
        self.__nota = nota
        self.__fecha = fecha or date.today().isoformat()
        self.__observacion = observacion

    def registrar_nota(self, nota: float) -> None:
        self.__nota = nota

    def actualizar_nota(self, nota: float) -> None:
        self.__nota = nota

    def consultar_nota(self) -> float:
        return self.__nota


class Horario:
    def __init__(self, id_horario: int, hora_inicio: str, hora_fin: str):
        self.__id_horario = id_horario
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin