from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv

	# @@ -27,6 +28,7 @@ def create_app(test_config=None):

###### Change this next line#######
# from flask import Flask


# def create_app(test_config=None):
#     app = Flask(__name__)

#     from .routes import hello_world_bp
#     app.register_blueprint(hello_world_bp)

#     return app

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import walking_buddy_bp
    app.register_blueprint(walking_buddy_bp)

    @walking_buddy_bp.route("/users", methods=["GET"])
    def get_users_json():
        return {
            "name": "Ada Lovelace",
            "message": "Hello!",
            "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
        }

    return app

