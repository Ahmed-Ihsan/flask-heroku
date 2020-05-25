from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import *
app = Flask(__name__)

data=User.query.all()
for r in data:
	print(r.name+"  "+r.email+"  "+r.city+"  "+r.password)