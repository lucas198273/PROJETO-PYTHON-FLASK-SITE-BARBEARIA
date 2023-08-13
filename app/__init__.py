from flask import Flask



app =Flask(__name__);
# app = arquivo onde estamos 
from app import rotas
app.config['SECRET_KEY'] = "palavra_secreta"

from app import rotas