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

        # JSON data
        self.bearer_tokens={
            "admin": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjgyZGFlN2I2YjkwYmY4MTg3MTdiIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU4OTc4MDkyOCwiZXhwIjoxNTg5Nzg4MTI4LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd5bXMiLCJkZWxldGU6Z3ltcyIsInJlYWQ6Z3ltcyIsInVwZGF0ZTpneW1zIl19.DnhvUO-_LnBxcSAhzfVavjPtD8RcuNbCakwPJFBy4EpPAGVUP46Lln00sxNz2DZeHQi1KJktyD6TQi7sWTdpCdqHnt6kv8WvuyfyLPLpat4CpF6gMIdFwWuSET23LduiItsLJcONioGBodar1sYjzFP7-0K6FZLdhyQddC5FB1j9sjKMb--28OKdJlNo346bnDH2NVmQT66DtDvGEKv2iyYp0IUntMlQwEzNoJ3g-98gFK0nXOu6_1h2pV5jNxdiAESwkm2MQtVodK-GEn_7nLOM5MJ13_F--mYFaNJWAkPF9zgdzud3zQgikRbP5s3wGywbgXfFWmKzkBokq0muVw",
            "user": ""
        }

        self.new_gym={
            "name":"Boulderwelt West",
            "address": "West-Straße 10",
            "city": 116,
            "website": "https://www.boulderwelt-muenchen-west.de/",
            "category": 1,
            "status": "closed"
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


    ''' Test
    ROUTE: ('/gyms/create')
    METHODS: POST
    '''
    def test_create_gym(self):
        res = self.client().post('/gyms/create', json=self.new_gym, headers={"Authorization" : self.bearer_tokens['admin']})
        print(res)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


    ''' Test
    ROUTE: ('/gyms')
    METHODS: GET
    '''
    def test_get_gyms(self):
        res = self.client().get('/gyms')
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
