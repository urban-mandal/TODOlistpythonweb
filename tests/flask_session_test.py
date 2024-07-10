from flask import Flask, session, config
import secrets_file


a = secrets_file.SecretsManeger()
app = Flask("__name__")
app.config.from_object(a.get_secretkey())
current_session = session()


@app.route("/")
def index():
    pass