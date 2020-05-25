# Project 1

The first project is a website to rate and review books and I use Goodreads for accurate results as the site contains 5,000 book reviews

## Youtube
https://youtu.be/WMlEPJFqhgY

## Web Programming with Python and JavaScript
### PYTHON
#### import.py
In this file, book data from title, author, year, and ISBN number is uploaded to a database

#### models.py
Databases are created using models.py file

#### delete_table.py
Used to delete a specific table

#### applicaton.py
Set the environment variable FLASK_APP to be application.py. On a Mac or on Linux, the command to do this is export FLASK_APP=application.py. On Windows, the command is instead set FLASK_APP=application.py. You may optionally want to set the environment variable FLASK_DEBUG to 1, which will activate Flask’s debugger and will automatically reload your web application whenever you save a change to a file.
Set the environment variable DATABASE_URL to be the URI of your database, which you should be able to see from the credentials page on Heroku.
Run flask run to start up your Flask application.

### HTML
#### page1.htnl
On this page, you can login to the website or go to page2.html page and create an account if you have not previously created an account.

#### page2.html
On this page, there are many fields for entering information such as username, password, email and city to create an account and login to the website

#### page3.html
On this page, you enter data such as title, author, year, or ISBN for a specific book to show you matching search results. If it is not present, you will not see any search results and if you search for something that is not in the search results, you will see the message 404

#### page4.html
On this page, you will see all book information from title, author, year, ISNB, website visitor reviews and reviews from Goodreads, and on this page you can add a review for a specific book

#### page5.html
/api/<ISBN>
{

"author":"Doug Lloyd",
"average_score":"4.14",
"isbn":"1632168146",
"review_count":7,
"title":"Memory",
"year":2015
}

### CSS
style.css for page1.html
style_2.css for page2.html
style_3.css for page3.html
style_4.css for page4.html