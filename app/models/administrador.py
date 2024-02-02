from app import db

class Administrador(db.Model):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    cedulaAdministrador = db.Column(db.String(45))
    nombreAdministrador = db.Column(db.String(45))
    AprellidoAdministrador = db.Column(db.String(45))
    telefonoAdministrador = db.Column(db.String(45))







    

