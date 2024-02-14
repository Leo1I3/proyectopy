from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.administrador import Administrador

auth_bp = Blueprint('session', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombreAdministrador = request.form['nombreAdministrador']
        contraseña = request.form['contraseña']
        
        user = Administrador.query.filter_by(nombreAdministrador=nombreAdministrador, contraseña=contraseña).first()

        if user:
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('equipo.index'))  # Corregir esta redirección
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('equipo.index')) 
    
    return redirect(url_for('administrador.index'))

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.nombreAdministrador}! This is your dashboard.'

@auth_bp.route('/logout', methods=['POST'])  # Añadir corchetes alrededor de 'POST'
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('administrador.index'))