from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://gqymvscekvfgty:44c3422f56f15fdfe08f2d8d4e1652c98be6b87fca411ca898f96bbe5f94d0ab@ec2-176-34-97-213.eu-west-1.compute.amazonaws.com:5432/d2afn869tf1fcb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False 
db = SQLAlchemy(app)
__tablename__= "books"

class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, unique=False, nullable=False)
    title = db.Column(db.String, unique=False, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String, unique=True, nullable=False)
	city = db.Column(db.String, unique=False, nullable=False)
	password = db.Column(db.String, unique=True, nullable=False)

class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	books_id= db.Column(db.Integer, unique=False,nullable=False)
	User_id= db.Column(db.Integer, unique=False ,nullable=False)
	bo_us= db.Column(db.Integer, unique=True ,nullable=False)
	Review_num = db.Column(db.Integer, unique=False, nullable=False)
	Review_text = db.Column(db.String, unique=False, nullable=False)
	User_name = db.Column(db.String, unique=False, nullable=False)

if __name__ == '__main__':
	Review_add=Review(books_id=0, User_id=0,bo_us=0,Review_num=5,Review_text="test",User_name="Ahmed Ihsan")
	db.session.add(Review_add)
	db.create_all()
	db.session.commit()



	
		