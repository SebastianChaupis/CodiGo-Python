from flask import Blueprint

portafolio = Blueprint('portafolio',__name__,url_prefix='/portafolio')

from . import views