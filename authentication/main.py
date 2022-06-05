import os
from urllib import response

from flask import Flask, make_response, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)

@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] in get_users() and get_users()[request.form['username']] == hash_password(request.form['password']):
            session['username'] = request.form['username']
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('username', request.form['username'])
            return resp
        else:
            error = 'Invalid username/password'
    return render_template('login.html',error=error)


@app.route("/dashboard")
def dashboard():
    username = request.cookies.get('username')
    return render_template('dashboard.html', username=username)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
