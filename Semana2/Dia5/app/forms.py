from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')
    
class ProyectoForm(FlaskForm):
    codigo = StringField('Codigo',validators=[DataRequired()])
    nombre = StringField('nombre',validators=[DataRequired()])
    descripcion = StringField('descripcion',validators=[DataRequired()])
    imagen = StringField('imagen',validators=[DataRequired()])
    url = StringField('url',validators=[DataRequired()])
    submit= SubmitField('Agregar')