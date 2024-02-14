from flask import Blueprint, request, render_template
from app import db
from app.models.administrador import Administrador

bp = Blueprint('administrador', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    data = Administrador.query.all()
    return render_template("welcome.html", data=data)

@bp.route('/add', methods=['POST'])
def add():
    try:
        cedulaAdministrador=request.form.get('cedulaAdministrador')
        nombreAdministrador=request.form.get('nombreAdministrador')
        AprellidoAdministrador=request.form.get('AprellidoAdministrador')
        telefonoAdministrador=request.form.get('telefonoAdministrador')
        contraseña=request.form.get('contraseña')
        
        new_admin = Administrador(cedulaAdministrador=cedulaAdministrador,nombreAdministrador=nombreAdministrador,AprellidoAdministrador=AprellidoAdministrador,telefonoAdministrador=telefonoAdministrador,contraseña=contraseña)
        db.session.add(new_admin)
        db.session.commit()
        return render_template("welcome.html")
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar administrador: {str(e)}", 500

@bp.route('/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        admin = db.session.query(Administrador).get(id)
        if admin:
            cedulaAdministrador=request.form.get('cedulaAdministrador')
            nombreAdministrador=request.form.get('nombreAdministrador')
            AprellidoAdministrador=request.form.get('AprellidoAdministrador')
            telefonoAdministrador=request.form.get('telefonoAdministrador')
            contraseña=request.form.get('contraseña')
        
            id = Administrador(cedulaAdministrador=cedulaAdministrador,nombreAdministrador=nombreAdministrador,AprellidoAdministrador=AprellidoAdministrador,telefonoAdministrador=telefonoAdministrador,contraseña=contraseña)
            db.session.commit()
            return render_template("welcome.html")
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
