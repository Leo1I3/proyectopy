from app import db

class SalidaEquipo(db.Model):
    __tablename__ = 'salida_equipo'
    idSalida = db.Column(db.Integer, primary_key=True)
    fechaSalida = db.Column(db.String(45))
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'))
    idAdministrador = db.Column(db.Integer, db.ForeignKey('administrador.idAdministrador'))
    usuario = db.relationship("Usuario")