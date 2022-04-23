from flask import Flask, render_template, request, session
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# URL ='https://api.github.com/users/SebastianChaupis'

app = Flask(__name__)

# Creacion de clave secreta para las variables de sesion
app.secret_key = 'qweasdzxc'


@app.route('/')
def index():
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()

    for doc in docBiografia:
        dicBiografia = doc.to_dict()

    session['biografia'] = dicBiografia

    colEnlaces = db.collection('enlaces')
    docEnlaces = colEnlaces.get()
    lstEnlaces= []
    for doc in docEnlaces:
        dicEnlaces = doc.to_dict()
        lstEnlaces.append(dicEnlaces)
        
    session['enlaces']= lstEnlaces
    # data = requests.get(URL)
    # nombre = request.args.get('nombre', 'no hay nombre')
    # context = data.json()

    return render_template('home.html')


@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA', 'ENCANTO', 'SONIC 2']
    nombre = request.args.get('nombre', 'no hay nombre')
    context = {
        'nombre': nombre,
        'peliculas': listaPeliculas
    }
    return render_template('peliculas.html', **context)

# RUTAS PARA PAGINA


@app.route('/acercade')
def about():
    return render_template('acercade.html')


@app.route('/portafolio')
def portafolio():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()
    # print (docProyectos)

    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)

    context = {
        'proyectos': lstProyectos
    }

    return render_template('portafolio.html', **context)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


app.run(debug=True)
