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

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}>'


class City(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey("state.id"), nullable=False)

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}>'


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    cities = db.relationship('City', backref="city", lazy=True)

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}>'


# class Country(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(), unique=True, nullable=False)

#     def __repr__(self):
#         return f'<Id: {self.id}; Name: {self.name}>'