import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session ,render_template , redirect ,url_for , request ,jsonify
from import_books.models import *
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json

name = " "
book_data=None

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database 1
'''engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))'''

# Set up database 2
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL") # or url
db = SQLAlchemy(app)

# Set up database 3
'''app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)'''


@app.route('/')
def login():
	return render_template('page1.html')

@app.route('/ch_account' , methods =['POST','GET'])
def login2():
	global name 
	name=request.form['name']
	passWord=request.form['Password']
	try:
		data=User.query.filter_by(name=name).first()
		if data.password == passWord:
			data=books.query.all()
			return render_template('page3.html' , book=data)
		else:
				return render_template('page1.html', error_login="The Password Error")
	except Exception as e :
		print(e)
		return render_template('page1.html', error_login="Something Error")

@app.route('/signin')
def first_signin():
	return render_template('page2.html')

@app.route('/signin2',  methods =['POST','GET'])
def signin():
	global name 
	name=request.form['name']
	passWord=request.form['Password']
	passWordC=request.form['PasswordC']
	city=request.form['city']
	email=request.form['email']
	if name == "":
		error="Enter Username "
		return render_template('page2.html',error_u=error)
	elif passWord =="":
		error="Enter Your Password"
		return render_template('page2.html',error_p=error)
	elif passWord != passWordC:
		error="Passwords Don't Match"
		return render_template('page2.html',error_pc=error)
	elif email =="":
		error="Enter Your Email"
		return render_template('page2.html',error_e=error)
	elif city =="":
		error="Enter Your City"
		return render_template('page2.html',error_c=error)
	else:
		try:
			us=User(name=name, email=email,city=city,password=passWord)
			db.session.add(us)
			db.create_all()
			db.session.commit()
			data=books.query.all()
			return render_template('page3.html' , book=data)
		except Exception as e:
			print(e)
			error_find="The account exists"
			return render_template('page2.html',error_find=error_find)


@app.route('/post' , methods =['POST','GET'])
def post():
	search=request.form['Search']
	try:
		global book_data
		book_data=books.query.all()
		for read in book_data:
			if read.isbn in search:
				book_data=books.query.filter_by(isbn=read.isbn).first()
				Review_d=Review.query.filter_by(books_id=read.id).all()
				# Goodreads
				res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
				resl=res.json()
				read_1=resl['books'][0]['work_ratings_count']
				read_2=resl['books'][0]['average_rating']
				read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
				return render_template('page4.html' ,book=book_data,Review_html=Review_d,inf=read_3)
			elif read.title in search:
				book_data=books.query.filter_by(title=read.title).first()
				Review_d=Review.query.filter_by(books_id=read.id).all()
				# Goodreads
				res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
				resl=res.json()
				read_1=resl['books'][0]['work_ratings_count']
				read_2=resl['books'][0]['average_rating']
				read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
				return render_template('page4.html' , book=book_data ,Review_html=Review_d,inf=read_3)
			elif read.author in search:
				book_data=books.query.filter_by(author=read.author).first()
				Review_d=Review.query.filter_by(books_id=read.id).all()
				# Goodreads
				res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
				resl=res.json()
				read_1=resl['books'][0]['work_ratings_count']
				read_2=resl['books'][0]['average_rating']
				read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
				return render_template('page4.html' , book=book_data ,Review_html=Review_d,inf=read_3)
			elif str(read.year) in search:
				book_data=books.query.filter_by(year=read.year).first()
				Review_d=Review.query.filter_by(books_id=read.id).all()
				# Goodreads
				res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
				resl=res.json()
				read_1=resl['books'][0]['work_ratings_count']
				read_2=resl['books'][0]['average_rating']
				read_3=['ratings: ',read_1,'Average Rating: ',read_2]
				return render_template('page4.html' , book=book_data ,Review_html=Review_d,inf=read_3)
			else:
				Error="404"
		data=books.query.all()
		return render_template('page3.html' , error="404",book=data)
	except Exception as e:
		data=books.query.all()
		return render_template('page3.html' , error="403" , book=data)

@app.route('/Send_Review' , methods =['POST','GET'])
def post_2():
	try:
	 	global name
	 	Review_n=request.form['Review_n']
	 	Review_t=request.form['Review_t']
	 	idUser=User.query.filter_by(name=name).first()
	 	bo_us=book_data.id+idUser.id
	 	Review_add=Review(books_id=book_data.id, User_id=idUser.id,bo_us=bo_us, Review_num=Review_n,Review_text=Review_t,User_name=name)
	 	try:
	 		db.session.add(Review_add)
	 		db.create_all()
	 		db.session.commit()
	 		Review_add=Review.query.filter_by(books_id=book_data.id).all()
	 		# Goodreads
	 		res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
	 		resl=res.json()
	 		read_1=resl['books'][0]['work_ratings_count']
	 		read_2=resl['books'][0]['average_rating']
	 		read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
	 		return render_template('page4.html' ,book=book_data ,Review_html=Review_add ,inf=read_3)
	 	except Exception as e:
	 		print(e)
	 		Review_add=Review.query.filter_by(books_id=book_data.id).all()
	 		# Goodreads
	 		res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
	 		resl=res.json()
	 		read_1=resl['books'][0]['work_ratings_count']
	 		read_2=resl['books'][0]['average_rating']
	 		read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
	 		return render_template('page4.html' ,book=book_data,Review_html=Review_add ,error="Error",inf=read_3)

	except Exception as e:
		print(e)
		Review_add=Review.query.filter_by(books_id=book_data.id).all()
		# Goodreads
		res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns": book_data.isbn})
		resl=res.json()
		read_1=resl['books'][0]['work_ratings_count']
		read_2=resl['books'][0]['average_rating']
		read_3=['Ratings: ',read_1,'Average Rating: ',read_2]
		return render_template('page4.html' ,book=book_data,Review_html=Review_add ,error="Something error" , inf=read_3)

@app.route('/api/<string:isbn>' , methods =['POST','GET'])
def API(isbn):
	try:
		book_data=books.query.filter_by(isbn=isbn).first()
		res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "Pye0fYSnJ6BFkmjNavZJlw", "isbns":isbn})
		resl=res.json()
		read_1=resl['books'][0]['reviews_count']
		read_2=resl['books'][0]['average_rating']
		data_json= {"title": book_data.title ,
		"author": book_data.author,
		"year": book_data.year ,
		 "isbn": book_data.isbn,
		 "review_count":read_1,
		 "average_score":read_2 }
		return jsonify(data_json)
	except Exception as e:
		return jsonify({'Error':404})