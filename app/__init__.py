from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import administrador_routes, detallesalida_routes,equipo_routes,salidaequipo_routes,usuario_routes
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(detallesalida_routes.bp)
    app.register_blueprint(equipo_routes.bp)
    app.register_blueprint(salidaequipo_routes.bp)
    app.register_blueprint(usuario_routes.bp)

    return app