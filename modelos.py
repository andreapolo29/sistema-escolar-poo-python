class Persona:
    def __init__(self, nombre, documento, correo):
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self.__nombre = nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo

    def mostrar_info(self):
        return f"{self.__nombre} (Doc: {self.__documento}) - {self.__correo}"


class Estudiante(Persona):
    def __init__(self, nombre, documento, correo, grado, colegio_actual):
        super().__init__(nombre, documento, correo)
        self.__grado = grado
        self.__colegio_actual = colegio_actual
        self.__estado = "Activo"

    def get_grado(self):
        return self.__grado

    def set_grado(self, grado):
        self.__grado = grado

    def get_colegio_actual(self):
        return self.__colegio_actual

    def set_colegio_actual(self, colegio):
        self.__colegio_actual = colegio

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def solicitar_traslado(self, colegio_destino):
        return f"Traslado solicitado de {self.__colegio_actual} hacia {colegio_destino}"

    def mostrar_info(self):
        return (
            f"Estudiante: {self.get_nombre()} | Grado: {self.__grado} | "
            f"Colegio: {self.__colegio_actual} | Estado: {self.__estado}"
        )


class Profesor(Persona):
    def __init__(self, nombre, documento, correo, materia):
        super().__init__(nombre, documento, correo)
        self.__materia = materia

    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    def mostrar_info(self):
        return f"Profesor: {self.get_nombre()} | Materia: {self.__materia}"


class Colegio:
    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__estudiantes = []

    def get_nombre(self):
        return self.__nombre

    def get_ciudad(self):
        return self.__ciudad

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def get_estudiantes(self):
        return self.__estudiantes

    def mostrar_info(self):
        return f"Colegio: {self.__nombre} ({self.__ciudad}) - Estudiantes: {len(self.__estudiantes)}"


class Traslado:
    def __init__(self, estudiante, colegio_origen, colegio_destino, motivo):
        self.__estudiante = estudiante
        self.__colegio_origen = colegio_origen
        self.__colegio_destino = colegio_destino
        self.__motivo = motivo
        self.__estado = "Pendiente"

    def get_estudiante(self):
        return self.__estudiante

    def get_colegio_origen(self):
        return self.__colegio_origen

    def get_colegio_destino(self):
        return self.__colegio_destino

    def get_motivo(self):
        return self.__motivo

    def get_estado(self):
        return self.__estado

    def aprobar(self):
        self.__estado = "Aprobado"
        self.__estudiante.set_colegio_actual(self.__colegio_destino)
        self.__estudiante.set_estado("Trasladado")

    def rechazar(self):
        self.__estado = "Rechazado"

    def mostrar_info(self):
        return (
            f"[{self.__estado}] {self.__estudiante.get_nombre()}: "
            f"{self.__colegio_origen} -> {self.__colegio_destino} ({self.__motivo})"
        )


class Solicitud:
    def __init__(self, persona, tipo, descripcion):
        self.__persona = persona
        self.__tipo = tipo
        self.__descripcion = descripcion
        self.__estado = "Pendiente"

    def get_persona(self):
        return self.__persona

    def get_tipo(self):
        return self.__tipo

    def get_descripcion(self):
        return self.__descripcion

    def get_estado(self):
        return self.__estado

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def mostrar_info(self):
        return (
            f"[{self.__estado}] {self.__tipo} de {self.__persona.get_nombre()}: "
            f"{self.__descripcion}"
        )