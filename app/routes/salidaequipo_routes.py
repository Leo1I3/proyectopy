from flask import Blueprint, request, render_template
from app import db
from app.models import SalidaEquipo

bp = Blueprint('salida_equipo', __name__)

@bp.route('/salidaequipo', methods=['GET', 'POST'])
def index():
    data = SalidaEquipo.query.all()
    return render_template("prestamo.html", data=data)
    


@bp.route('/salidaequipo/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        new_salida_equipo = SalidaEquipo(
            fechaSalida=data['fechaSalida'],
            idusuario=data['idusuario'],
            idAdministrador=data['idAdministrador']
        )
        db.session.add(new_salida_equipo)
        db.session.commit()
        return "Salida de equipo agregada correctamente", 201
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar salida de equipo: {str(e)}", 500

@bp.route('/salidaequipo/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        data = request.get_json()
        salida_equipo = db.session.query(SalidaEquipo).get(id)
        if salida_equipo:
            salida_equipo.fechaSalida = data['fechaSalida']
            salida_equipo.idusuario = data['idusuario']
            salida_equipo.idAdministrador = data['idAdministrador']
            db.session.commit()
            return "Salida de equipo editada correctamente", 200
        else:
            return "Salida de equipo no encontrada", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar salida de equipo: {str(e)}", 500

@bp.route('/salidaequipo/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        salida_equipo = db.session.query(SalidaEquipo).get(id)
        if salida_equipo:
            db.session.delete(salida_equipo)
            db.session.commit()
            return "Salida de equipo eliminada correctamente", 200
        else:
            return "Salida de equipo no encontrada", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar salida de equipo: {str(e)}", 500
