from flask import Blueprint, request, render_template
from app import db
from app.models import Usuario

bp = Blueprint('usuario', __name__)

@bp.route('/usuario', methods=['GET', 'POST'])
def index():
    data = Usuario.query.all()
    return render_template("usuario.html", data=data)

@bp.route('/usuario/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        new_usuario = Usuario(
            nombre=data['nombre'],
            contraseña=data['contraseña']
        )
        db.session.add(new_usuario)
        db.session.commit()
        return "Usuario agregado correctamente", 201
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar usuario: {str(e)}", 500

@bp.route('/usuario/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        data = request.get_json()
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            usuario.nombre = data['nombre']
            usuario.contraseña = data['contraseña']
            db.session.commit()
            return "Usuario editado correctamente", 200
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar usuario: {str(e)}", 500

@bp.route('/usuario/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return "Usuario eliminado correctamente", 200
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar usuario: {str(e)}", 500    