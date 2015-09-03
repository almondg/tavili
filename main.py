import sys
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__, static_folder="public")
db = MongoEngine()