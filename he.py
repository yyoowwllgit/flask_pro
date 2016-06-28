#new add
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'mydb.db')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db= SQLAlchemy(app)
class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(80),unique=True)
	email=db.Column(db.String(120),unique=True)
	def __init__(self,uname,email):
		self.username=uname
		self.email=email
	def __repr__(self):
		return '<User %r>'% self.username

