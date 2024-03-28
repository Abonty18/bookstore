from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Book, User, Order

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///bookstore.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Home page
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Online Bookstore</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f8f9fa;
            }
            h1 {
                color: #0d6efd;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin-bottom: 10px;
            }
            a {
                text-decoration: none;
                color: #0d6efd;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Online Bookstore!</h1>
        <p>Choose an option:</p>
        <ul>
            <li><a href="/books">View All Books</a></li>
            <li><a href="/register">Register</a></li>
            <li><a href="/add_book">Add a Book</a></li>
        </ul>
    </body>
    </html>
    """


# Route to display all books
@app.route('/books')
def display_books():
    books = session.query(Book).all()
    return render_template('books.html', books=books)

# Route to display book details
@app.route('/books/<int:book_id>')
def book_details(book_id):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        return render_template('book_details.html', book=book)
    else:
        return 'Book not found.'

# Route to handle user registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # You can add code to handle user registration here
        return redirect(url_for('home'))
    else:
        return render_template('register.html')

# Route to add a book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = int(request.form['price'])
        # Create a new book object
        new_book = Book(title=title, author=author, price=price)
        # Add the new book to the database
        session.add(new_book)
        session.commit()
        return redirect(url_for('display_books'))
    else:
        return """
        <html>
        <head>
            <title>Add a Book</title>
        </head>
        <body>
            <h1>Add a Book</h1>
            <form action="/add_book" method="post">
                <label for="title">Title:</label><br>
                <input type="text" id="title" name="title" required><br><br>
                <label for="author">Author:</label><br>
                <input type="text" id="author" name="author" required><br><br>
                <label for="price">Price:</label><br>
                <input type="number" id="price" name="price" required><br><br>
                <input type="submit" value="Add Book">
            </form>
        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True)
