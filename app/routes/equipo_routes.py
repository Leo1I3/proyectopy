from flask import Blueprint, request, render_template
from app import db
from app.models import Equipo

bp = Blueprint('equipo', __name__)

@bp.route('/equipo', methods=['GET', 'POST'])
def index():
    data = Equipo.query.all()
    return render_template("equipo.html", data=data)

@bp.route('/equipoxd', methods=['GET'])
def XD():
    return render_template("nosotros.html")

@bp.route('/equipo/add', methods=['POST'])
def add():
    try:
        marcaE = request.form.get('marcaE')
        codigoE = request.form.get('codigoE')
        colorE = request.form.get('colorE')
        despE = request.form.get('despE')
        estadoE = request.form.get('estadoE')
        estadoE = estadoE == '1'

        new_equipo = Equipo(marcaE=marcaE, codigoE=codigoE, colorE=colorE, despE=despE, estadoE=estadoE)
        db.session.add(new_equipo)
        db.session.commit()
        return render_template("equipo.html") 
        
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar equipo: {str(e)}", 500

@bp.route('/equipo/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        equipo = db.session.query(Equipo).get(id)
        if equipo:
            marcaE = request.form.get('marcaE')
            codigoE = request.form.get('codigoE')
            colorE = request.form.get('colorE')
            despE = request.form.get('despE')
            estadoE = request.form.get('estadoE')
            id = Equipo(marcaE=marcaE, codigoE=codigoE, colorE=colorE, despE=despE, estadoE=estadoE)
            db.session.edit(id)
            db.session.commit()
            return "Equipo editado correctamente", 200
        else:
            return "Equipo no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar equipo: {str(e)}", 500

@bp.route('/equipo/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        equipo = db.session.query(Equipo).get(id)
        if equipo:
            db.session.delete(equipo)
            db.session.commit()
            return "Equipo eliminado correctamente", 200
        else:
            return "Equipo no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar equipo: {str(e)}", 500
