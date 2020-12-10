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
    return render_template('cover_page.html',reviews=reviews)

@bp.route('/list')
def List():
    reviews = Review.query.all()
    return render_template('review_list.html',reviews=reviews)