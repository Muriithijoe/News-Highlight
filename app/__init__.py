from flask import Flask
from .config import DevConfig

app = Flask(__name__)

app.config.from_object(Devconfig)
app.config.from_object('config.py')

from app import views
