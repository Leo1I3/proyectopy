from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config["SECRET_KEY"]= os.urandom(24)
    
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "administrador.index"

    @login_manager.user_loader
    def load_user(idAdministrador):
        from app.models.administrador import Administrador
        administrador = Administrador.query.get(int(idAdministrador))
        return administrador
    
    from app.routes import administrador_routes, detallesalida_routes,equipo_routes,salidaequipo_routes,usuario_routes, session_routes
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(detallesalida_routes.bp)
    app.register_blueprint(equipo_routes.bp)
    app.register_blueprint(salidaequipo_routes.bp)
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(session_routes.auth_bp)

    return app