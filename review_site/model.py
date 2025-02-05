# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-12-06 20:16:39
#  * @modify date 2020-12-06 20:16:39
#  * @desc [모델. 객체를 정의함]
#  */


from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 게시물 ID
    subject = db.Column(db.String(200), nullable=False) # 게시물 제목
    content = db.Column(db.Text(), nullable=False) # 게시물 컨텐츠
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일자
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('post_set'))

    def __init__(self,subject,content,user):
        self.subject = subject
        self.content = content
        self.create_date = datetime.datetime.now()
        self.user = user

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 댓글 ID
    reivew_id = db.Column(db.Integer, db.ForeignKey('review.id', ondelete='CASCADE'))
    # review의 id에 종속되어 삭제시 같이 삭제됨
    reivew = db.relationship('Review', backref=db.backref('review_set'))
    # 참조할 모델 / 역참조 모델
    creator = db.Column(db.String)
    content = db.Column(db.Text(), nullable=False) # 댓글
    create_date = db.Column(db.DateTime(), nullable=False) # 작성일시

    def __init__(self,content,creator):
        self.content = content
        self.create_date = datetime.datetime.now()
        self.creator = creator

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)