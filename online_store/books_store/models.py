from online_store import db

book_genre = db.Table('book_genre',
                        db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                        db.Column('genre.id', db.Integer, db.ForeignKey('genre.id')))


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship('Book', backref='author')

    def __init__(self, name):
        self.name = name


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String)
    
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    genres = db.relationship('Genre', secondary=book_genre, backref='books')

    def __init__(self, title, price, amount, image_path, author):
        self.title = title
        self.price = price
        self.amount = amount
        self.image_path = image_path
        self.author = author


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name