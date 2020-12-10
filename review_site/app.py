# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-12-06 20:10:04
#  * @modify date 2020-12-06 20:10:04
#  * @desc [페이지의 메인. BP를 이용한 라우팅 / 프로젝트 앱 전체 관리를 담당함]
#  */

from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_wtf.csrf import CSRFProtect

from model import *
import config

app = Flask(__name__)
# csrf = CSRFProtect()
# csrf.init_app(app)

# DB 설정
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app,db)

# markdown
Markdown(app, extensions=['nl2br', 'fenced_code'])


from views import main, review, comment, auth
app.register_blueprint(main.bp)
app.register_blueprint(review.bp)
app.register_blueprint(comment.bp)
app.register_blueprint(auth.bp)

    

    










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