from flask import Flask
from markupsafe import escape
from flask import render_template, request, jsonify, url_for, config, session, redirect
import sqlite3
import databasecoms as dbc
import secrets_file 
import databasesecurity as dbs


a = secrets_file.SecretsManeger()
app = Flask("__name__")
# app.config.from_object(a.get_secretkey())
# session_current = session()
login_status = ""

@app.route("/")
def index():
    global login_status
    dbc.tasks_db_initiate()
    if login_status == "true":
        print("Works but doesnt work")
        return render_template("./index.html")
    return render_template("./login.html")

@app.route("/form", methods=["POST"])
def form():
    pass


@app.route("/loadTasks", methods=["GET", "POST"])
def get_tasks(id):
    return jsonify(dbc.load_tasks(id))

@app.route("/login", methods=["POST"])
def login():
    global login_status
    dbs.db_users_initiate()
    username = request.form.get("username")
    password = request.form.get("password")
    if dbs.user_login(username, password) == True:
        print("Login was correct but the tamplate didnt get rendered")
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
