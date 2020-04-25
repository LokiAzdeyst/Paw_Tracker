"""
The flask application package.
"""

from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine
from flask_wtf import FlaskForm



app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {"db":"PawTracker"}
app.config['SECRET_KEY']  = 'my super secret key'

admin = Admin(app)
db = MongoEngine(app)
import Paw_Tracker.views



app.run()