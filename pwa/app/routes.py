# routes.py
from flask import Blueprint, render_template, request, redirect, url_for

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return redirect(url_for('routes.signup'))

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Add your user creation logic here
        return redirect(url_for('routes.login'))
    return render_template('signup.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Add your login validation logic here
        return redirect(url_for('routes.dashboard'))
    return render_template('login.html')

@routes.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')