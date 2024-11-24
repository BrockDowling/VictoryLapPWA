# auth.py
from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # Add your login validation logic here
        # For now, just redirect to dashboard
        return redirect(url_for('routes.dashboard'))
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('routes.index'))