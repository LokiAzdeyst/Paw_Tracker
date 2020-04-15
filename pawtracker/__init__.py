"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Paw_Tracker.views
