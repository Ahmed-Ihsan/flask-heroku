from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from models import *
app = Flask(__name__)

data=Review.query.all()
for r in data:
	print(r.id,r.books_id,r.User_id,r.bo_us,r.Review_num,r.Review_text)