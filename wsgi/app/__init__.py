import os
from flask import Flask
import pymongo
from pymongo import MongoClient
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'secret_key'

client = MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
db = client[os.environ['OPENSHIFT_APP_NAME']]

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'signin'


from app import views , models