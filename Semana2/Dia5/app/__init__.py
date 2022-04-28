from flask import Flask

from flask_bootstrap import Bootstrap
#Importamos blueprints
from .admin import admin
from .portafolio import portafolio 


from .config import Config

def create_app():
    app = Flask(__name__)    
    
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    
    #Con este codigo estamos agregando admin al proyecto principal
    app.register_blueprint(admin)
    app.register_blueprint(portafolio)
    return app