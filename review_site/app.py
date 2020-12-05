from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate

from model import *
import os
import config
import datetime


app = Flask(__name__)
# DB 설정
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///board'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///board'
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
# app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config.from_object(config)
# SQLALCHEMY_TRACK_MODIFICATIONS = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    reviews = Review.query.all()
    # SELECT * FROM reviews ORDER BY id DESE;
    return render_template('index.html',reviews=reviews)

@app.route('/reviews/new')
def new():
    return render_template('new.html')

@app.route('/reviews/create', methods=["POST"])
def create():
    # title = request.args.get('title')
    subject = request.form.get('subject')
    # content = request.args.get('content')
    content = request.form.get('content')
    review = Review(subject=subject, content=content)
    db.session.add(review)
    db.session.commit()
    
    # return render_template('create.html')
    return redirect('/reviews/{}'.format(review.id))
    
@app.route('/reviews/<int:id>')
def read(id):
    # id를 찾지 못하면 404 반환
    review = Review.query.get_or_404(id)
    # SELECT * FROM reviews WHERE id=1;
    return render_template('read.html',review=review)
    
@app.route('/reviews/<int:id>/delete') 
def delete(id):
    review = Review.query.get(id)
    # DELETE FROM reviews WHERE id=3;
    db.session.delete(review)
    db.session.commit()
    
    return redirect('/')
    
@app.route('/reviews/<int:id>/edit')
def edit(id):
    review = Review.query.get_or_404(id)
    return render_template('edit.html',review=review)
    
@app.route('/reviews/<int:id>/update', methods=["POST"])
def update(id):
    review = Review.query.get_or_404(id)
    review.title = request.form.get('title')
    review.content = request.form.get('content')
    db.session.commit()
    
    return redirect('/reviews/{}'.format(id))
    
@app.route('/reviews/<int:review_id>/comments',methods=['POST'])
def comments(review_id):
    content = request.form.get('content')
    creator = request.form.get('creator')
    comment = Comment(content,creator)
    review = Review.query.get_or_404(review_id)
    review.review_set.append(comment)
    db.session.add(comment)
    db.session.commit()
    
    return redirect('/')
    
@app.route('/comment/<int:id>/delete')
def comment_delete(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect('/')









# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

# import config

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(config)

#     # ORM
#     db.init_app(app)
#     migrate.init_app(app, db)
#     import model

#     from views import main
#     app.register_blueprint(main.bp)

#     return app