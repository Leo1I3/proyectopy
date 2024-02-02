from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import administrador_routes, detallesalida_routes,equipo_routes,salidaequipo_routes,usuario_routes
