import os

from flask import (
    Flask, 
    request, 
    abort, 
    jsonify, 
    abort,
    redirect) 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database.models import (
    setup_db,
    db,
    User, City, State, Category, Gym, Status)
from database.data import (
    Country
)

# -------------------------------------------------------------------- #
# Functions.
# -------------------------------------------------------------------- #

def get_gym(id):
    ''' 
    Returns a gym object.
    :param id: int.
    :return: a sql alchemy object.
    '''
    gym = Gym.query.filter(Gym.id == id).one_or_none()
    if gym == None: 
        abort(404)

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

# -------------------------------------------------------------------- #
# Flask App.
# -------------------------------------------------------------------- #
def create_app(test_config=None):
    ''' Initializes the API.
    For further information check out the README.md. This function includes:
        - App conifguration.
        - Data to initialize the app.
        - Controller.
        - Error handler.
    '''
    # -------------------------------------------------------------------- #
    # App config.
    # -------------------------------------------------------------------- #

    # create and configure the app
    
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # setup CORS

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    
    # -------------------------------------------------------------------- #
    # Data to initialize the app.
    # -------------------------------------------------------------------- #

    if (len(State.query.all()) == 0) and (len(City.query.all()) == 0):

        c1 = Country('Germany')
        c1_info = c1.get_states_and_cities()  
    
        try:   
            for state in list(c1_info.keys()):
                new_state = State(name=state)
                db.session.add(new_state)
            
            for state in list(c1_info.keys()):
                state_in_table = State.query.filter(State.name == state).one_or_none()
                if state_in_table is None:
                    print('Could not add cities')
                else:
                    for city in c1_info[state]:
                        new_city = City(name=city, state_id=state_in_table.id)
                        db.session.add(new_city)
            
            db.session.commit()

        except Exception:
            db.session.rollback()
            abort(422)
           
    else:
        print('=> Cities and States are loaded')


    if len(Status.query.all()) == 0:
        db.session.add_all([
            Status(description='open'),
            Status(description='closed')
        ])
        db.session.commit()

    else:
        print('=> Categories are loaded')


    # -------------------------------------------------------------------- #
    # Controller.
    # -------------------------------------------------------------------- #

    @app.route('/')
    def public_index():
        return redirect('gyms', 302)


    @app.route('/gyms', methods=["GET"])
    def get_gyms():
        ''' Returns a JSON with all gyms '''
        data = Gym.query.all()
        body = []
        for gym in data: 
            body.append(gym.formatted())
        
        return jsonify(body)


    @app.route('/gyms/create', methods=["POST"])
    def create_gym():
        ''' Creates a new gym in the database
        INPUT: JSON formatted string that contains name, address, city, website and category. 
        '''
        try: 
            body = request.get_json()
            print(body)
            new_gym = Gym(
                name = str(body['name']), 
                address = str(body['address']),
                city_id = get_city_id(body['city']),
                website = str(body['website']),
                category_id = get_category_id(body['category']),
                status_description = str(body['status'])
                )
            new_gym.insert()

            return jsonify({
                "success": True,
                "message": f"Successfully added {new_gym.name} to Database"
            })
        
        except KeyError:
            abort(422)

    
    @app.route('/gyms/<int:id>', methods=['PATCH'])
    def update_gym(id):
        '''
        Update a existing gym with its correspondent id
        '''
        gym = get_gym(id)
        try: 
            body = request.get_json()
            print(body)
            gym.name = str(body['name'])
            gym.address = str(body['address'])
            gym.city_id = get_city_id(body['city'])
            gym.website = str(body['website'])
            gym.category_id = get_category_id(body['category'])
            gym.status_description = str(body['status'])
            gym.update()

            return jsonify({
                "success": True,
                "message": f"Successfully updated {gym.name}"
            })

        except (KeyError, AttributeError): 
            abort(422)


    @app.route('/gyms/<int:id>', methods=['DELETE'])
    def delete_gym(id):
        '''
        Deletes the gym with the correspondent id
        '''
        gym = get_gym(id)
        try: 
            gym.delete()

            return jsonify({
                "message": "success"
            })

        except Exception:
            db.session.rollback()
            abort(422)

    # -------------------------------------------------------------------- #
    # Error handler.
    # -------------------------------------------------------------------- #

    @app.errorhandler(404)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
            }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    return app

      
APP = create_app()

if __name__ == '__main__':    
    APP.run(host='0.0.0.0', port=8080, debug=True)


