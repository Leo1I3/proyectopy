from flask import Blueprint, request, render_template,url_for,redirect
from app import db
from app.models.usuario import Usuario 

bp = Blueprint('usuario', __name__)

@bp.route('/usuario', methods=['GET', 'POST'])
def index():
    data = Usuario.query.all()
    return render_template("usuario.html", data=data)

@bp.route('/usuario/add', methods=['POST'])
def add():
    try:
        nombre=request.form.get('nombre')
        correo=request.form.get('correo')
        cedula=request.form.get('cedula')
        

        new_usuario = Usuario(nombre=nombre,correo=correo,cedula=cedula)
        db.session.add(new_usuario)
        db.session.commit()
        return redirect(url_for('usuario.index'))
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar usuario: {str(e)}", 500

@bp.route('/usuario/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        usuario = db.session.query(Usuario).get(id)
        if usuario:
            nombre=request.form.get('nombre')
            correo=request.form.get('correo')
            cedula=request.form.get('cedula')
        

            id = usuario(nombre=nombre,correo=correo,cedula=cedula)
            db.session.commit()
            return redirect(url_for('usuario.index'))
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar usuario: {str(e)}", 500

@bp.route('/usuario/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        usuario = Usuario.query.get_or_404(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return redirect(url_for('usuario.index'))
        else:
            return "Usuario no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar usuario: {str(e)}", 500    