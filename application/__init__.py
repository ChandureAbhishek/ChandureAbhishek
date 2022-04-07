
from flask import Flask,render_template,redirect,url_for
# from flask_cors import CORS
# from flask_sqlalchemy  import SQLAlchemy
import hashlib
# from flask_login import UserMixin

app = Flask(__name__)

# data_app= Flask(__name__)
# CORS(app)
# app.config['SECRET_KEY'] = b'b0087d2daf02efa9ae1bac36aa886f1e'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://maestroAkaunto:Ec7u3jKMOX3sQB77cqokXH9mL6CragQ2X9hE5Ec5@platformdatabases.cwcrw9wfkhgr.us-east-1.rds.amazonaws.com/sit_ecom3"
# db = SQLAlchemy(app)
# SQLALCHEMY_TRACK_MODIFICATIONS = True

from application import routes

