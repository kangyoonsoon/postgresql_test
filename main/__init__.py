from flask import Flask,request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()    # take .env file
url = os.getenv("DATABASE_URL")
print("url: ", url)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # https://stackoverflow.com/questions/24727902/what-is-the-form-of-my-local-postgresql-database-url
    app.config['SQLALCHEMY_DATABASE_URI'] = url

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

