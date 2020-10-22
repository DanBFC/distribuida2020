from flask import Flask, request, render_template, redirect, url_for
from MongoDBController import MongoDB

mongo = MongoDB()

app = Flask(__name__)

#Bibliotecas para autenticacion
from flask_jwt import JWT, jwt_required, current_identity
import jwt as encorder
import datetime
from datetime import timedelta

@app.route("/", methods=["GET"])
def root():
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        userdb = mongo.find_user(username)
        if userdb:
            if password == userdb['password']:
                userdb['_id'] = str(userdb['_id'])
                return render_template("usuario.html", user=userdb, bitacora=userdb['bitacora'])
        return render_template("error401.html")
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == 'POST':
        usuario = {
            'fullname': request.form['fullname'],
            'username': request.form['username'],
            'password': request.form['password'],
            'estado': request.form['estado'],
            'sexo': request.form['gender'],
            'edad': request.form['edad']
        }
        usuario = mongo.insert_user(usuario)
        usuario['_id'] = str(usuario['_id'])
        return render_template("usuario.html", user=usuario, bitacora=usuario['bitacora'])
    return render_template("registro.html")

@app.route("/actividad", methods=["POST"])
def actividad():
    user_id = request.form['userId']
    activity = {
        'distance': request.form['distancia'],
        'time': request.form['time'],
        'type': request.form['tipo'],
        'date': request.form['date'],
    }
    userdb = mongo.insert_activity(activity, user_id)
    return render_template("usuario.html", user=userdb, bitacora=userdb['bitacora'])

if __name__ == '__main__':
    app.run()
