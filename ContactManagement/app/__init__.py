from flask import Flask
from config import Config

chimera_app = Flask(__name__)
chimera_app.config.from_object(Config)

from app import routes