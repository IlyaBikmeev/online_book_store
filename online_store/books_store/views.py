from flask import render_template

from online_store import app


@app.route('/')
def test():
    return render_template('content.html')