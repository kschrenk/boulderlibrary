import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

database_name = "boulderlibrary_test"
database_path = os.environ['DATABASE_BASE_URL'] + database_name

db = SQLAlchemy()

# ------------------------------------------------ #
#  Models.
# ------------------------------------------------ #

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.app = app
    db.init_app(app)
    db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


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


# ------------------------------------------------ #
#  Getter and Setter
# ------------------------------------------------ #

def get_gym(id):
    ''' 
    Returns a gym object.
    :param id: int.
    :return: a sql alchemy object.
    '''
    gym = Gym.query.filter(Gym.id == id).one_or_none()

    return gym 


def get_city_id(na):
    ''' 
    Returns the id of a city.
    :param name: str.
    :return: the city's id.
    '''
    city_id = City.query.filter(City.name == na).one_or_none().id
    if city_id == None:
        abort(404)
    
    return city_id


def get_category_id(descr):
    '''
    Returns the id of a gym category.
    :param descr: str.
    :return: the category's id.
    '''
    category_id = Category.query.filter(Category.description == str(descr)).one_or_none().id
    if category_id == None:
        abort(404)
    
    return category_id