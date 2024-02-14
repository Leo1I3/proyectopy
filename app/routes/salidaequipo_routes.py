from flask import Blueprint, request, render_template,url_for,redirect
from app import db
from app.models.salidaequipo import SalidaEquipo
from app.models.usuario import Usuario
from app.models.administrador import Administrador
from app.models.equipo import Equipo

bp = Blueprint('salida_equipo', __name__)

@bp.route('/salidaequipo', methods=['GET', 'POST'])
def index():
    data = SalidaEquipo.query.all()
    data1 = Usuario.query.all()
    data2 = Administrador.query.all()
    data3 = Equipo.query.all()
    return render_template("prestamo.html", data=data, data1=data1, data2=data2, data3=data3)

@bp.route('/salidaequipo/add', methods=['POST'])
def add():
    try:
        fechaSalida=request.form.get('fechaSalida')
        idusuario=request.form.get('idusuario')
        idAdministrador=request.form.get('idAdministrador')
        idequipo=request.form.get('idequipo')

        new_salida_equipo = SalidaEquipo(fechaSalida=fechaSalida, idusuario=idusuario, idAdministrador=idAdministrador,idequipo=idequipo)
        db.session.add(new_salida_equipo)
        equipo = Equipo.query.get_or_404(new_salida_equipo.idequipo)
        if equipo:
            equipo.estadoE = True
        db.session.commit()
        return redirect(url_for('salida_equipo.index'))
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar salida de equipo: {str(e)}", 500

@bp.route('/salidaequipo/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        salida_equipo = db.session.query(SalidaEquipo).get(id)
        if salida_equipo:
            fechaSalida=request.form.get('fechaSalida')
            idusuario=request.form.get('idusuario')
            idAdministrador=request.form.get('idAdministrador')

            id = SalidaEquipo(fechaSalida=fechaSalida, idusuario=idusuario, idAdministrador=idAdministrador)
            db.session.commit()
            return redirect(url_for('salida_equipo.index'))
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
