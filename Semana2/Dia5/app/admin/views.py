from multiprocessing import context
from flask import (
    render_template,
    redirect,url_for,
    session,flash)

from . import admin

#Importamos los formularios
from app.forms import LoginForm

#Autenticacion ########
import pyrebase 
from app.auth_token import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
############
@admin.route('/')
def index():
    if('token' in session):
        return render_template('admin/index.html')
    else:
        return redirect(url_for('admin.login'))
@admin.route('/login',methods=['GET','POST'])
def login():
    login_forms = LoginForm()
    context={
        'login_forms':login_forms
    }
    
    ##CODIFO PARA LOGIN  DE USUSARIOS 
    if login_forms.validate_on_submit():
        usuarioData = login_forms.usuario.data
        passwordData = login_forms.password.data
        
        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            dataUsuarioValido = auth.get_account_info(usuario['idToken'])
            print (dataUsuarioValido)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
        except:
            print ("Usuario Incorrecto")
            flash("Usuario o password invalidos")
            
    return render_template('admin/login.html',**context)