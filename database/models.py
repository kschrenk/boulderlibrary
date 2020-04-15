import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app):

    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ['DATABASE_URI']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.app = app
    db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)




