from flask import Flask


def create_app():
    app = Flask(__name__)

    from views import main
    app.register_blueprint(main.bp)

    return app

# # 실행
# if __name__ == "__main__":
#     create_app()
#     app.run()
