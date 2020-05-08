import os
import unittest
from flask_sqlalchemy import SQLAlchemy
from app import create_app

class BoulderlibraryTestCase(unittest.TestCase):
    '''This class represents the boulder library test case'''

    def setUp(self):
        '''Define test variables and initialize the app'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        setup_db(self.app, self.database_path)

    # JSON Data

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
    ROUTE: ('/main/gyms')
    METHODS: GET
    '''
    def test_start_search(self):
        res = self.client().get('/main/gyms')
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
