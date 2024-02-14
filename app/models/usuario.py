from app import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    correo = db.Column(db.String(45))
    cedula = db.Column(db.String(45))
    salida = db.relationship('SalidaEquipo', lazy='dynamic')