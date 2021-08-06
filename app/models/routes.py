from flask_sqlalchemy.model import camel_to_snake_case
# from tests.test_wave_01 import test_create_task_must_contain_description
from flask import Blueprint
from app import db
# from app.models.task import Task
# from app.models.goal import Goal
from flask import request, Blueprint, make_response, jsonify
# from datetime import datetime
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    return app

walking_buddy_bp = Blueprint("Walking_Buddy", __name__)

@blueprint_name.route("/endpoint/path/here", methods=["GET"])
def endpoint_name():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

