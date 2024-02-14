from app import db


class Equipo(db.Model):
    __tablename__ = 'equipo'
    idequipo = db.Column(db.Integer, primary_key=True)
    marcaE = db.Column(db.String(45))
    codigoE = db.Column(db.String(45))
    colorE = db.Column(db.String(45))
    despE = db.Column(db.String(45))
    estadoE = db.Column(db.Boolean)
    salida = db.relationship('SalidaEquipo')