import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.app = app
    db.init_app(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}>'


class City(db.Model): 
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    state_id = Column(Integer, db.ForeignKey("state.id"), nullable=False)
    gyms = db.relationship('Gym', backref="city", lazy=True)

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}; State_Id: {self.state_id}>'


class State(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    cities = db.relationship('City', backref="state", lazy=True)

    def __repr__(self):
        return f'<Id: {self.id}; Name: {self.name}>'


class Gym(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    address = Column(String(), unique=True, nullable = False)
    website = Column(String(), nullable=False)
    city_id = Column(Integer(), db.ForeignKey("city.id"), nullable=False)
    status_description = Column(String(12), db.ForeignKey("status.description"), nullable=False)  
    category_id = Column(Integer(), db.ForeignKey("category.id"), nullable=False)

    def __repr__(self):
        return f'<Id: {self.id};\nName: {self.name};\nAdress: {self.address}>'

    def formatted(self):
        formatted_gym = {}
        formatted_gym['id'] = self.id
        formatted_gym['name'] = self.name
        formatted_gym['address'] = self.address
        formatted_gym['website'] = self.website
        formatted_gym['city'] = self.city.name
        formatted_gym['category'] = self.category.description
        formatted_gym['status'] = self.status.description
        return formatted_gym
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Status(db.Model):
    description = Column(String(12), primary_key=True)
    gyms = db.relationship('Gym', backref="status", lazy=True)


class Category(db.Model):
    id = Column(Integer(), primary_key=True)
    description = Column(String(40))
    gyms = db.relationship('Gym', backref="category", lazy=True)

    def __repr__(self):
        return f'<Id: {self.id}; Description: {self.description}>'



