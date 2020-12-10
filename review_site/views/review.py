# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-12-06 20:03:40
#  * @modify date 2020-12-06 20:03:40
#  * @desc [리뷰 페이지의 view를 담당. 동작함수를 포함함]
#  */

from flask import Blueprint, render_template, request, redirect

from model import *

bp = Blueprint('review', __name__, url_prefix='/reviews')

@bp.route('/new')
def new():
    return render_template('new.html')

@bp.route('/create', methods=["POST"])
def create():
    # title = request.args.get('title')
    subject = request.form.get('subject')
    # content = request.args.get('content')
    content = request.form.get('content')
    review = Review(subject=subject, content=content)
    db.session.add(review)
    db.session.commit()
    
    # return render_template('create.html')
    return redirect('/')
    
@bp.route('/<int:id>')
def read(id):
    # id를 찾지 못하면 404 반환
    review = Review.query.get_or_404(id)
    # SELECT * FROM reviews WHERE id=1;
    return render_template('read.html',review=review)
    
    
@bp.route('/<int:id>/delete') 
def delete(id):
    review = Review.query.get(id)
    # DELETE FROM reviews WHERE id=3;
    db.session.delete(review)
    db.session.commit()
    
    return redirect('/')
    
@bp.route('/<int:id>/edit')
def edit(id):
    review = Review.query.get_or_404(id)
    return render_template('edit.html',review=review)
    
@bp.route('/<int:id>/update', methods=["POST"])
def update(id):
    review = Review.query.get_or_404(id)
    review.title = request.form.get('title')
    review.content = request.form.get('content')
    db.session.commit()
    
    return redirect('/reviews/{}'.format(id))

@bp.route('/<int:review_id>/comments',methods=['POST'])
def comments(review_id):
    content = request.form.get('content')
    creator = request.form.get('creator')
    comment = Comment(content,creator)
    review = Review.query.get_or_404(review_id)
    review.review_set.append(comment)
    db.session.add(comment)
    db.session.commit()
    
    return redirect('/')