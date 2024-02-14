from app import db
from flask_login import UserMixin

class Administrador(db.Model,UserMixin):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    cedulaAdministrador = db.Column(db.String(45))
    nombreAdministrador = db.Column(db.String(45))
    AprellidoAdministrador = db.Column(db.String(45))
    telefonoAdministrador = db.Column(db.String(45))
    contraseña = db.Column(db.String(45))



    def get_id(self):
        return self.idAdministrador







    

