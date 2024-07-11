from flask import Flask
from markupsafe import escape
from flask import render_template, request, jsonify, url_for, config, session, redirect
import sqlite3 as sq
import databasecoms as dbc
import secrets_file 
import databasesecurity as dbs
from databasefolder import get_database_loc


app = Flask("__name__")
app.config.from_pyfile("secrets_file.py")
login_status = ""
dbc.tasks_db_initiate()
dbs.db_users_initiate()


@app.route("/")
def index():
    global login_status
    if login_status == "true":
        return render_template("index.html")
    return render_template("login.html")

@app.route("/form", methods=["POST"])
def form():
    pass


@app.route("/loadTasks", methods=["GET", "POST"])
def get_tasks(id):
    return jsonify(dbc.load_tasks(id))

@app.route("/login", methods=["POST"])
def login():
    global login_status
    username = request.form.get("username")
    password = request.form.get("password")
    username = username.strip()
    password = password.strip()
    if dbs.user_login(username, password) == True:
        con = sq.connect(get_database_loc())
        cur = con.cursor()
        res = cur.execute("SELECT id FROM loginInfo WHERE username= ?", (username,))
        session["username"] = username
        session["id"] = res.fetchall()[0][0]
        print(session["username"], session["id"])
        login_status = "true"
        return jsonify(success=True)
    else:
        return  jsonify(success=False)
    
@app.route("/Singup", methods=["POST"])
def singup():
    dbs.db_users_initiate()
    username = request.form.get("username")
    password = request.form.get("password")
    dbs.add_user(username, password)
    return "singup succesful"


@app.route("/logout", methods=["GET"]) 
def logout():
    global login_status
    session.pop("username", None)
    session.pop("id", None)
    login_status = "false"
    return jsonify(success=True)