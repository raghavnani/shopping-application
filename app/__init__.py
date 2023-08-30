from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_cors import CORS

config = os.environ.get("CONFIG_MODULE", "config.connection")

app = Flask(__name__)
app.config.from_object(config)
# cors = CORS(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.models.models import *
# from app.models.user import User

# Build the database:
# This will create the database file using SQLAlchemy

with app.app_context():
    db.create_all()
    db.session.commit()