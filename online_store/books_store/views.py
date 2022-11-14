from online_store import app
from online_store.books_store.models import *
from flask import jsonify


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
