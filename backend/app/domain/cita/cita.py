import uuid
from datetime import date, time
from .disponibilidad import Profesional
from .especialidad import Especialidad
from .paciente import Paciente

class Cita:
    def __init__(self, paciente: Paciente, profesional: Profesional, especialidad: Especialidad, fecha: date, hora: time):
        self.id = str(uuid.uuid4())
        self.paciente = paciente
        self.profesional = profesional
        self.especialidad = especialidad
        self.fecha = fecha
        self.hora = hora
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def __repr__(self):
        return (
            f"<Cita {self.id} | Paciente: {self.paciente.nombre}, "
            f"Profesional: {self.profesional.nombre}, Especialidad: {self.especialidad.nombre}, "
            f"Fecha: {self.fecha}, Hora: {self.hora}, Estado: {self.estado}>"
        )
