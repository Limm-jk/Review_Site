from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    from views import main
    app.register_blueprint(main.bp)

    return app

# # 실행
# if __name__ == "__main__":
#     create_app()
#     app.run()
