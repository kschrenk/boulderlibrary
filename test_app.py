import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, User, City, State, Gym, Status, Category


class BoulderlibraryTestCase(unittest.TestCase):
    '''This class represents the boulder library test case'''

    def setUp(self):
        '''Define test variables and initialize the app'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "boulderlibrary_test"
        self.database_path = os.environ['DATABASE_BASE_URL'] + self.database_name
        setup_db(self.app, database_path=self.database_path)


        # JSON Data
        self.bearer_tokens={
            "admin": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjgyZGFlN2I2YjkwYmY4MTg3MTdiIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU4OTk1MDA2NiwiZXhwIjoxNTg5OTU3MjY2LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd5bXMiLCJkZWxldGU6Z3ltcyIsInVwZGF0ZTpneW1zIl19.fzsrPnI1J29Xusdi-wFwdTby4SO9dzX74unUSt7p0BhGahC_mchNqfSN5RFlK1IW95y0-ZLfX-P_sO6mhfohK0WPkSF7xslI5U5mI-TrsrT3M8QDRnGGGhwf90-XIJvGER7VyH2Y3h3IK7xaOQ89nTCglNlMXhiLvIulr0oCALNdAto0jEgBFWAVI6gB-dY9IoDRiDkhp2wI99aUaT6oYoGwD4IUBiuPhrSJoNYSpxuotfTucxDjYCZdRo8S4S7zST9oBuUjY-j-Z4Hja88g07wwS3o27HN9aejnyZOZ_6iRiW1HOtzjXZlKlr35-WmoCc6MZN85cZ7kD3AbFgEN4g",
            "user": " Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMzc4MDU0MDdmMjgwYmVkYjMwZTRjIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU4OTg2ODcxNiwiZXhwIjoxNTg5ODc1OTE2LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZmF2b3I6Z3ltcyIsImdldDpmYXZvdXJpdGVfZ3ltcyIsInJlbW92ZTpmYXZvdXJpdGVfZ3ltcyJdfQ.h9E2Ga_VYI_lcNEfFWfbvzE-qqR0DnA1PHEcFW0Z5ZXZy4zc879B9BjKpXP7WcLrruSpr7fhNnYUkY01FSho8lvNYQaSSWSkW-bCkcrvxTC9K-bfnFqcYQ_-3MOxIsl2HvzQxDouIw7iXx0rKcaQRyChmUJUhmefIR8Fwqdawxr91_CkxK8Wi1dAF6bluBXCYVHXkORKdX1XqGvmkfh00IjXoWB6tWlYArP60p7Zc1M1rRaiSB47S8TVua7K0DyipYIw8IN95rhKv2QU-Qqzh5frnHB-3oGM5BzayPRNOmriaVzLCmaUtFfkeacsarL6Xv0q6BtkpjeDFn8WXTQBDA"
        }

        self.new_gym={
            "name":"Blockhelden Bamberg",
            "address": "Memmelsdorfer Str. 211",
            "website": "https://www.blockhelden.de/",
            "city": 145,
            "status": "closed",
            "category": 1
        }

        self.edit_gym={
            "name":"Boulderwelt Regensburg",
            "address": "Im Gewerbepark A46",
            "website": "https://www.boulderwelt-regensburg.de/",
            "city": 121,
            "status": "closed",
            "category": 1
        }

        # Binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    

    def tearDown(self):
        '''Executed after each test'''
        pass


    # ----------------------------------------------------- #
    # Admin. 
    # ----------------------------------------------------- #

    ''' Test
    ROUTE: ('/gyms/create')
    METHODS: POST
    '''
    def test_create_gym(self):
        res = self.client().post('/gyms/create', json=self.new_gym, headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


    def test_401_if_auth_header_is_missing(self):
        res = self.client().post('/gyms/create', json=self.new_gym)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["description"], 'Authorization header is expected.')    
    

    ''' Test
    ROUTE: ('/gyms/<int:id>')
    METHODS: PATCH, DELETE
    '''
    def test_update_gym(self):
        res = self.client().patch('gyms/16', json=self.edit_gym, headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


    def test_422_if_wrong_id(self):
        res = self.client().patch('gyms/160', json=self.edit_gym, headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)


    def test_delete_gym(self):
        res = self.client().delete('gyms/1', headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


    def test_422_if_id_does_not_exist(self):
        res = self.client().delete('gyms/10000', headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)


    # ----------------------------------------------------- #
    # Main. 
    # ----------------------------------------------------- #

    ''' Test
    ROUTE: ('/gyms')
    METHODS: GET
    '''
    def test_get_gyms(self):
        res = self.client().get('/gyms')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)


    def test_404_if_route_does_not_exist(self):
        res = self.client().get('/gymss')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)


    # ----------------------------------------------------- #
    # User. 
    # ----------------------------------------------------- #

    







# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
