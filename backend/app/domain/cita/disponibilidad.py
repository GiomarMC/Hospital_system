from datetime import date, time
from .especialidad import Especialidad

class Profesional:
    def __init__(self, id: str, nombre: str, especialidad: Especialidad):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.agenda = {}

    def agregar_disponibilidad(self, fecha: date, hora: time):
        fecha_str = fecha.isoformat()
        if fecha_str not in self.agenda:
            self.agenda[fecha_str] = []
        if hora not in self.agenda[fecha_str]:
            self.agenda[fecha_str].append(hora)

    def esta_disponible(self, fecha: date, hora: time) -> bool:
        fecha_str = fecha.isoformat()
        return fecha_str in self.agenda and hora in self.agenda[fecha_str]

    def reservar_hora(self, fecha: date, hora: time):
        """Marca la hora como ya reservada (la elimina de la agenda)."""
        fecha_str = fecha.isoformat()
        if self.esta_disponible(fecha, hora):
            self.agenda[fecha_str].remove(hora)

    def obtener_agenda(self, fecha: date):
        fecha_str = fecha.isoformat()
        return self.agenda.get(fecha_str, [])

    def __repr__(self):
        return f"<Profesional {self.nombre} ({self.especialidad.nombre})>"
