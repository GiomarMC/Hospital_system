from flask import Blueprint, request, jsonify
from datetime import datetime, date, time

from app.aplication.services.agenda_cita_service import AgendaCitaService
from app.domain.cita.paciente import Paciente
from app.domain.cita.especialidad import Especialidad
from app.domain.cita.disponibilidad import Profesional

cita_bp = Blueprint("cita", __name__)
service = AgendaCitaService()

especialidad_demo = Especialidad("ESP001", "Cardiología")
profesional_demo = Profesional("PROF001", "Dr. Juan Pérez", especialidad_demo)
profesional_demo.agregar_disponibilidad(date(2025, 7, 29), time(10, 0))
profesional_demo.agregar_disponibilidad(date(2025, 7, 29), time(11, 0))


@cita_bp.route("/citas", methods=["POST"])
def crear_cita():
    data = request.json
    try:
        paciente = Paciente(data["paciente_id"], data["paciente_nombre"], data["paciente_email"])

        fecha = datetime.strptime(data["fecha"], "%Y-%m-%d").date()
        hora = datetime.strptime(data["hora"], "%H:%M").time()

        cita = service.crear_cita(paciente, profesional_demo, especialidad_demo, fecha, hora)

        return jsonify({
            "mensaje": "Cita registrada exitosamente.",
            "cita_id": cita.id,
            "estado": cita.estado
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@cita_bp.route("/disponibilidad", methods=["GET"])
def verificar_disponibilidad():
    fecha_str = request.args.get("fecha")
    hora_str = request.args.get("hora")

    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        hora = datetime.strptime(hora_str, "%H:%M").time()
        disponible = profesional_demo.esta_disponible(fecha, hora)

        return jsonify({
            "profesional": profesional_demo.nombre,
            "fecha": fecha_str,
            "hora": hora_str,
            "disponible": disponible
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@cita_bp.route("/agenda", methods=["GET"])
def obtener_agenda():
    fecha_str = request.args.get("fecha")
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        agenda = profesional_demo.obtener_agenda(fecha)
        horas = [h.strftime("%H:%M") for h in agenda]

        return jsonify({
            "profesional": profesional_demo.nombre,
            "fecha": fecha_str,
            "horas_disponibles": horas
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400
