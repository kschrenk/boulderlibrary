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
            "admin": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjgyZGFlN2I2YjkwYmY4MTg3MTdiIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU4OTg3MDEzMywiZXhwIjoxNTg5ODc3MzMzLCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd5bXMiLCJkZWxldGU6Z3ltcyIsInVwZGF0ZTpneW1zIl19.lu2RsD8E59oqbrA87hOJyBLeWR3zgwrmLZ08t2LdiXZURyYWBqez8XJbBJR8jlXiHMm2hncPNlaTFbpnh3v7v4xHJGOe2WnVncHcggf7z-IgxQfItAXL0dzrjrFjKx4pFJR4ZiNRfv-YMnf3rvPtqtq-0etyI46zbUPEcq-Bstx4MKEbTSHq6GvFQq74a1sQ7ZmbrYMWREnGf5o-Rn8sXYkZYfuhQSEoIYhujtwLmi9q3Magh5HfkRa9N6HFVsUxsyZ-fwYpqqwAZudZcfXQkPWACK-HzEoY-OGCan2XDNWH5xH5B-GyoudMe7QwrjixdIlJwkxadsm3XNN3O-819A",
            "user": " Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMzc4MDU0MDdmMjgwYmVkYjMwZTRjIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU4OTg2ODcxNiwiZXhwIjoxNTg5ODc1OTE2LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZmF2b3I6Z3ltcyIsImdldDpmYXZvdXJpdGVfZ3ltcyIsInJlbW92ZTpmYXZvdXJpdGVfZ3ltcyJdfQ.h9E2Ga_VYI_lcNEfFWfbvzE-qqR0DnA1PHEcFW0Z5ZXZy4zc879B9BjKpXP7WcLrruSpr7fhNnYUkY01FSho8lvNYQaSSWSkW-bCkcrvxTC9K-bfnFqcYQ_-3MOxIsl2HvzQxDouIw7iXx0rKcaQRyChmUJUhmefIR8Fwqdawxr91_CkxK8Wi1dAF6bluBXCYVHXkORKdX1XqGvmkfh00IjXoWB6tWlYArP60p7Zc1M1rRaiSB47S8TVua7K0DyipYIw8IN95rhKv2QU-Qqzh5frnHB-3oGM5BzayPRNOmriaVzLCmaUtFfkeacsarL6Xv0q6BtkpjeDFn8WXTQBDA"
        }

        self.new_gym={
            "name":"Boulderwelt West",
            "address": "West-Straße 10",
            "city": 116,
            "website": "https://www.boulderwelt-muenchen-west.de/",
            "category": 1,
            "status": "closed"
        }

        self.new_gym_edit={
            "name":"Boulderwelt West",
            "address": "West-Straße 10",
            "city": 116,
            "website": "https://www.boulderwelt-muenchen-west.de/",
            "category": 1,
            "status": "open"
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
    # App. 
    # ----------------------------------------------------- #

    ''' Test
    ROUTE: ('/data/init')
    METHODS: POST
    '''
    def test_init_data(self):
        res = self.client().post('/data/init', json={"country":"Germany"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['country'])
        self.assertTrue(data['status'])
        self.assertTrue(data['categories'])

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

    # ----------------------------------------------------- #
    # Admin. 
    # ----------------------------------------------------- #

    # ''' Test
    # ROUTE: ('/gyms/create')
    # METHODS: POST
    # '''
    # def test_create_gym(self):
    #     res = self.client().post('/gyms/create', json=self.new_gym, headers={"Authorization" : self.bearer_tokens['admin']})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    

    # ''' Test
    # ROUTE: ('/gyms/<int:id>')
    # METHODS: PATCH
    # '''
    # def test_update_gym(self):
    #     res = self.client().patch('gyms/1', json=self.new_gym_edit, headers={"Authorization" : self.bearer_tokens['admin']})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)


    # ''' Test
    # ROUTE: ('/gyms/<int:id>')
    # METHODS: DELETE
    # '''
    # def test_delete_gym(self):
    #     res = self.client().delete('gyms/1', headers={"Authorization" : self.bearer_tokens['admin']})
    #     data = json.loads(res.data)
        
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)


    # ----------------------------------------------------- #
    # User. 
    # ----------------------------------------------------- #


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
