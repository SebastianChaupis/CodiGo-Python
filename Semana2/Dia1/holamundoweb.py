from flask import Flask,request

#creamos objeto de la clase flask 
app = Flask(__name__)

#creamos mi primera ruta
@app.route('/')
def index():
    return '<center><h1>Hola Mundo Flask</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<center><h1>Hola {}</h1></center>'.format(nombre)

@app.route('/suma')
def suma():
    n1 = request.args.get('n1',0)
    n2= request.args.get('n2',0)
    resultado = int(n1)+int(n2)
    return '<h1>La suma de {}+{}= {}</h1>'.format(n1,n2,resultado)

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0,n2=0):
    resultado = n1 - n2
    return '<h1>La suma de {}-{}= {}</h1>'.format(n1,n2,resultado)
#Desplegamos nuestra app web
app.run(debug=True)