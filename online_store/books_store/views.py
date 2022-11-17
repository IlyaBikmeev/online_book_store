from online_store import app
from online_store.books_store.models import *
from flask import jsonify, render_template


@app.route('/')
def index():
    return render_template('content.html')

@app.route('/api/books/<int:book_id>')
def get_info(book_id):
    book_info = db.session.query(Book).get(book_id)
    if book_info:
        return jsonify(
            id=book_info.id,
            title=book_info.title,
            price=book_info.price,
            amount=book_info.amount,
            image_path=book_info.image_path,
            author_id=book_info.author.id,
            genre=[g.name for g in book_info.genres]
        )
    else:
        return jsonify()
      
@app.route('/api/books')
def get_all_books():
    result = []
    all_books = Book.query.all()
    for book in all_books:
        my_json = {"id": book.id,
            "title": book.title,
            "price": book.price,
            "amount": book.amount,
            "image_path": book.image_path,
            "author_id": book.author.id,
            "genre": [gen.name for gen in book.genres]}
        result.append(my_json)
    return jsonify(result)
  