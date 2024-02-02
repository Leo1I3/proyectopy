from flask import Blueprint, request, render_template
from app import db
from app.models import DetalleSalida

bp = Blueprint('detalle_salida', __name__)

@bp.route('/detallesalida', methods=['GET', 'POST'])
def index():
    data = DetalleSalida.query.all()
    return render_template("devolucion.html", data=data)

@bp.route('/detallesalida/add', methods=['POST'])
def add():
    try:
        data = request.get_json()
        new_detalle_salida = DetalleSalida(
            fechaEntregaDetalleSalida=data['fechaEntregaDetalleSalida'],
            idSalida=data['idSalida'],
            idequipo=data['idequipo']
        )
        db.session.add(new_detalle_salida)
        db.session.commit()
        return "Detalle de salida agregado correctamente", 201
    except Exception as e:
        db.session.rollback()
        return f"Error al agregar detalle de salida: {str(e)}", 500

@bp.route('/detallesalida/edit/<int:id>', methods=['PUT'])
def edit(id):
    try:
        data = request.get_json()
        detalle_salida = db.session.query(DetalleSalida).get(id)
        if detalle_salida:
            detalle_salida.fechaEntregaDetalleSalida = data['fechaEntregaDetalleSalida']
            detalle_salida.idSalida = data['idSalida']
            detalle_salida.idequipo = data['idequipo']
            db.session.commit()
            return "Detalle de salida editado correctamente", 200
        else:
            return "Detalle de salida no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al editar detalle de salida: {str(e)}", 500

@bp.route('/detallesalida/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        detalle_salida = db.session.query(DetalleSalida).get(id)
        if detalle_salida:
            db.session.delete(detalle_salida)
            db.session.commit()
            return "Detalle de salida eliminado correctamente", 200
        else:
            return "Detalle de salida no encontrado", 404
    except Exception as e:
        db.session.rollback()
        return f"Error al eliminar detalle de salida: {str(e)}", 500
