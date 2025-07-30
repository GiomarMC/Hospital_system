from datetime import date, time
from app.domain.cita.cita import Cita
from app.domain.cita.paciente import Paciente
from app.domain.cita.disponibilidad import Profesional
from app.domain.cita.especialidad import Especialidad
from app.infraestructure.adapters.external.sgc_adapter import enviar_notificacion_email

class AgendaCitaService:
    def __init__(self):
        self.citas_registradas = []  # Simulación de BD en memoria

    def crear_cita(self, paciente: Paciente, profesional: Profesional, especialidad: Especialidad, fecha: date, hora: time) -> Cita:
        if not profesional.esta_disponible(fecha, hora):
            raise Exception(f"El profesional {profesional.nombre} no está disponible en {fecha} a las {hora}")

        # Crear cita
        cita = Cita(paciente, profesional, especialidad, fecha, hora)
        self.citas_registradas.append(cita)

        # Marcar hora como reservada
        profesional.reservar_hora(fecha, hora)

        # Simular notificación
        enviar_notificacion_email(paciente, cita)

        return cita

    def obtener_agenda_profesional(self, profesional: Profesional, fecha: date):
        return profesional.obtener_agenda(fecha)

    def consultar_citas(self):
        return self.citas_registradas
