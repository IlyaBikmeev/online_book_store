from online_store import db

book_genre = db.Table('book_genre',
                        db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                        db.Column('genre.id', db.Integer, db.ForeignKey('genre.id')))


order_book = db.Table('order_book',
                      db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
                      db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
                      db.Column('amount', db.Integer))


order_step = db.Table('order_step',
                      db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
                      db.Column('step_id', db.Integer, db.ForeignKey('step.id')),
                      db.Column('date', db.DateTime))


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
    orders = db.relationship('Order', secondary=order_book, backref='books')

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


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_city = db.Column(db.String, nullable=False)
    days_delivery = db.Column(db.Integer, nullable=False)
    clients = db.relationship('Client', backref='city')

    def __init__(self, name_city, days_delivery):
        self.name_city = name_city
        self.days_delivery = days_delivery


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    steps = db.relationship('Step', secondary=order_step, backref='orders')

    def __init__(self, client):
        self.client = client


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_step = db.Column(db.String, nullable=False)

    def __init__(self, name_step):
        self.name_step = name_step


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    login = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    orders = db.relationship('Order', backref='client')

    def __init__(self, first_name, last_name, email, login, password_hash, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login = login
        self.password_hash = password_hash
        self.city = city
