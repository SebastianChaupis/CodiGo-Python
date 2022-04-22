from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    nombre = request.args.get('nombre', 'no hay nombre')
    
    context = {
        'nombre': nombre
    }
    return render_template('home.html', **context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA', 'ENCANTO', 'SONIC 2']
    nombre = request.args.get('nombre', 'no hay nombre')
    context ={
        'nombre':nombre,
        'peliculas':listaPeliculas
    }
    return render_template('peliculas.html',**context)
app.run(debug=True)
