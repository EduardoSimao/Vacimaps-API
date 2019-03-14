
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)


from app.models.table_cidade import Cidade
from app.models.table_doenca import Doenca
from app.models.table_doenca_cidade import Doenca_Cidade
from app.models.table_usuario import Usuario
from app.models.table_vacina import Vacina
from app.models.table_usuario_vacina import Usuario_Vacina
from app.models.table_vacina_doenca import Vacina_Doenca

db.create_all()




from app.controller.usuario import *
from app.controller.login import *
from app.controller.cidade import *
#from app.controllers.palestra.routes import palestras_blueprint



#app.register_blueprint(users_blueprint)
#app.register_blueprint(palestras_blueprint)



