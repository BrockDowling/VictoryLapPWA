# auth.py
from flask import Blueprint, render_template, request, redirect, url_for
import bycrypt 
import psycopg
from psycopg import connect
from dotenv import load_dotenv
import os 

load_dotenv()

auth = Blueprint('auth', __name__)
DBURL = os.getenv("DATABASE_URL")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form.get('email')
        password = request.form.get('password')
        with connect(DBURL) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT password from User WHERE email = user_email')
                user_pass = cur.fetchall()
        if bycrypt.compare(password, user_pass):
            return redirect(url_for('routes.dashboard'))
        return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('routes.index'))