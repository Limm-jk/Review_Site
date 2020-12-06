from flask import Blueprint, render_template

from model import *

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Work!'


@bp.route('/')
def index():
    reviews = Review.query.all()
    # SELECT * FROM reviews ORDER BY id DESE;
    return render_template('index.html',reviews=reviews)