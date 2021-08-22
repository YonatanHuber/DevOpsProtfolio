from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

chimera_app = Flask(__name__)
chimera_app.config.from_object(Config)
db = SQLAlchemy(chimera_app)
migrate = Migrate(chimera_app, db)

from app import routes, models