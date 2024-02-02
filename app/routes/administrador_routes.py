from flask import Blueprint, request, render_template
from app import db
from app.models import Administrador

bp = Blueprint('administrador', __name__)

@bp.route('/')
def index():
    data = Administrador.query.all()
    return render_template("welcome.html", data=data)

@bp.route('/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        new_admin = Administrador(
            cedulaAdministrador=data['cedulaAdministrador'],
            nombreAdministrador=data['nombreAdministrador'],
            AprellidoAdministrador=data['AprellidoAdministrador'],
            telefonoAdministrador=data['telefonoAdministrador']
        )
        db.session.add(new_admin)
        db.session.commit()
        return "Admin agregado correctamente", 201
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar administrador: {str(e)}", 500

@bp.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        data = request.get_json()
        admin = db.session.query(Administrador).get(id)
        if admin:
            admin.cedulaAdministrador = data['cedulaAdministrador']
            admin.nombreAdministrador = data['nombreAdministrador']
            admin.AprellidoAdministrador = data['AprellidoAdministrador']
            admin.telefonoAdministrador = data['telefonoAdministrador']
            db.session.commit()
            return "Administrador editado correctamente", 200
        else:
            return "Administrador no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar administrador: {str(e)}", 500

@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        admin = db.session.query(Administrador).get(id)
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return "Administrador eliminado correctamente", 200
        else:
            return "Administrador no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar administrador: {str(e)}", 500
