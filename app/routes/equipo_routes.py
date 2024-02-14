from flask import Blueprint, redirect, request, render_template, url_for
from app import db
from app.models import equipo
from app.models.equipo import Equipo

bp = Blueprint('equipo', __name__)

@bp.route('/equipo', methods=['GET', 'POST'])
def index():
    data = Equipo.query.all()
    print(data)
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

        return redirect(url_for('equipo.index'))
        
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar equipo: {str(e)}", 500

@bp.route('/equipo/edit/<int:id>', methods=['POST'])
def edit(id):
    try:
        Equipo = equipo.query.get_or_404(id)
        if Equipo:
            Equipo.estadoE = False
            db.session.commit()
            return redirect(url_for('devolucion.index'))
        else:
            return "Pc no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar Pc: {str(e)}", 500

@bp.route('/equipo/delete/<int:id>', methods=['POST'])
def delete(id):
    try:
        equipo = Equipo.query.get_or_404(id)
        if equipo:
            db.session.delete(equipo)
            db.session.commit()
            return redirect(url_for('equipo.index'))
        else:
            return redirect(url_for('equipo.index'))
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar equipo: {str(e)}", 500
