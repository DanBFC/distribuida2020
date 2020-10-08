from flask import Flask, request, render_template
from MongoDBController import MongoDB

mongo = MongoDB()

app = Flask(__name__)

#Bibliotecas para autenticacion
from flask_jwt import JWT, jwt_required, current_identity
import jwt as encorder
import datetime
from datetime import timedelta

bitacora = [{'distance': '16 kms', 'time': '1 hrs', 'type': 'Fondo', 'date': '2020-01-01'}, {'distance': '16 kms', 'time': '1 hrs', 'type': 'Fondo', 'date': '2020-01-01'}]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        userdb = mongo.find_user(username)
        if userdb:
            if password == userdb['password']:
                return render_template("usuario.html", user=userdb, bitacora=bitacora)
        return render_template("error401.html")
    return render_template("login.html", username='', user_id=0)

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == 'POST':
        usuario = {
            'username': request.form['fullname'],
            'username': request.form['username'],
            'password': request.form['password'],
            'estado': request.form['estado'],
            'sexo': request.form['gender'],
            'edad': request.form['edad']
        }
        usuario = mongo.insert_user(usuario)
        #print(usuario)
        return render_template("index.html", username=usuario['username'], user_id=usuario['_id'])
        #return request
    return render_template("registro.html")


if __name__ == '__main__':
    app.run()
