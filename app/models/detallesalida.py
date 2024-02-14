from app import db

class DetalleSalida(db.Model):
    __tablename__ = 'detalle_salida'
    idDetalleSalida = db.Column(db.Integer, primary_key=True)
    fechaEntregaDetalleSalida = db.Column(db.String(45))
    idSalida = db.Column(db.Integer, db.ForeignKey('salida_equipo.idSalida'))
    idequipo = db.Column(db.Integer, db.ForeignKey('equipo.idequipo'))
    salida_equipo = db.relationship("SalidaEquipo")
    equipo = db.relationship("Equipo")