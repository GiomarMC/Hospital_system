from app.domain.cita.cita import Cita
from app.domain.cita.paciente import Paciente

def enviar_notificacion_email(paciente: Paciente, cita: Cita):
    print("📧 Simulando envío de email...")
    print(f"Para: {paciente.email}")
    print(f"Asunto: Confirmación de Cita Médica")
    print(f"Hola {paciente.nombre}, tu cita ha sido registrada con éxito.")
    print(f"📅 Fecha: {cita.fecha}")
    print(f"⏰ Hora: {cita.hora}")
    print(f"👨‍⚕️ Profesional: {cita.profesional.nombre}")
    print(f"🩺 Especialidad: {cita.especialidad.nombre}")
    print("Gracias por confiar en nuestro sistema de salud.")
    print("-" * 50)