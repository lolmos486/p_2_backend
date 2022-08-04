from flask import Flask
from flask_session import Session
from controller.user_controller import uc
from controller.review_controller import rc
from controller.book_controller import bc


if __name__ == '__main__':

    app = Flask(__name__)
    app.secret_key = "hello"

    app.register_blueprint(uc)
    app.register_blueprint(bc)
    app.register_blueprint(rc)

    app.run(port=8080, debug=True)