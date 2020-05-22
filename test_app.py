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
            "admin": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjgyZGFlN2I2YjkwYmY4MTg3MTdiIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU5MDEzODA4MSwiZXhwIjoxNTkwMTQ1MjgxLCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd5bXMiLCJkZWxldGU6Z3ltcyIsInVwZGF0ZTpneW1zIl19.l0cTGZMazVXnDwA0Ln3R3h1PkS98C7zC6Mcmtph_GSHtegON9J20Wq0dIL-CwqPRVhHEsx2Fdh_xaewTdIxnx4wYVCH1NGgG7vT86mt13z14gF7KYXvMBlSfy3kdXqsWKllwSZhsouOvH659r73XR_Dzy-FBU9PnjZY4MTaTOj4t3YQYPTLy_hGfZGh06rmIcY9m3rl7efyV4a9RZ8KTIJwCMicDXlNtFvvgiPc4QOfTJADVqr-q6CRN8hNqA9JCkNYkGO46O24R9--LuZD0dfX5wHHWOV0VezEUID6Y3sIwbEu885jrmPDvT7WgJQ_6mn9ENs2kYHiPyIf0qI7-eA",
            "user": " Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FWkROREJGUWtWR1JrWXlRelJHTURnNE1qZzBPVFEwUlRNMU1qRXdSVE0wUmpFNU56Y3pNZyJ9.eyJpc3MiOiJodHRwczovL2Rldi13ZDcxNGQ4aC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjMzc4MDU0MDdmMjgwYmVkYjMwZTRjIiwiYXVkIjoiYm91bGRlciIsImlhdCI6MTU5MDEzNzE2NiwiZXhwIjoxNTkwMTQ0MzY2LCJhenAiOiJYZGx3NXRMRlJ0aGpoOW81N2UyNUhuRnlqSWttM0RkaCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZmF2b3I6Z3ltcyIsImdldDpmYXZvdXJpdGVfZ3ltcyIsInJlbW92ZTpmYXZvdXJpdGVfZ3ltcyJdfQ.DvdHFHElVx63aDaFck4VY9Il0f3VGm7PQr62rCM02p1llVyYcFPtQ0sJmaNEMaftVkQhSj6MlR4h5Doa6Q5a_YF9tIETcu1IL6Y1v2Y3RDXzSLVwQgKpENwRGzZxayle_Oce6w8RlLl9D1fYvcCZ1BVK7WJ_mvx9OrPZm_3iQF-oNayYnfSV4QVpK9aj5vKx8Vn_Wl0Mp_yZXfJDPmOT6u80O-UQCdLTFYZwh5ZewSeoBLsnMfMKkkSuq2sHRHKRftpMnyWVG-OFaRJG3jxCBcqooz0Cnb-dkmGbmto2t66FPwJW0wdqkVW4gdqAZJC48n-7_QQz63oTxUCSd7P1Mw"
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

        self.new_user={
            "user": "Jhonny",
            "last_name": "Walker"
        }

        self.new_user2={
            "user": "Jhonny",
            "last_name": "Waaaaaaaaaadfglksglkadfglkadlfkgkdfgkasdglker"
        }

        self.add_favs={
            "user_id": 2,
	        "gym_id": 6
        }

        self.add_wrong_favs={
            "user_id": 2,
	        "gym_id": 600
        }

        self.rem_favs={
            "user_id": 2,
	        "gym_id": 16
        }

        self.rem_error_favs={
            "user_id": 2,
	        "gym_id": 160
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


    def test_401_if_permission_not_found(self):
        res = self.client().post('/gyms/create', json=self.new_gym, headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["code"], "unauthorized")


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

        self.assertEqual(res.status_code, 422)


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

    ''' Test
    ROUTE: ('/user/create')
    METHODS: POST
    '''
    def test_create_user(self):
        res = self.client().post('/user/create', json=self.new_user)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_422_if_last_name_exceeds_character_limit(self):
        res = self.client().post('/user/create', json=self.new_user2)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)


    ''' Test
    ROUTE: ('/user/2/favourites')
    METHODS: GET
    '''
    def test_get_favourite_gyms(self):
        res = self.client().get('/user/2/favourites', headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_401_if_auth_header_is_missing(self):
        res = self.client().get('/user/2/favourites')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)


    ''' Test
    ROUTE: ('/user/favourites/add')
    METHODS: POST
    '''
    def test_add_gym_to_favourites(self):
        res = self.client().post('/user/favourites/add', json=self.add_favs, headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_404_if_wrong_key(self):
        res = self.client().post('/user/favourites/add', json=self.add_wrong_favs, headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_401_if_permission_not_found(self):
        res = self.client().post('/user/favourites/add', json=self.add_favs, headers={"Authorization" : self.bearer_tokens['admin']})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["code"], "unauthorized")

    ''' Test
    ROUTE: ('/user/favourites/remove')
    METHODS: DELETE
    '''
    def test_remove_gym(self):
        res = self.client().delete('/user/favourites/remove', json=self.rem_favs, headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


    def test_404_if_value_error(self):
        res = self.client().delete('/user/favourites/remove', json=self.rem_error_favs, headers={"Authorization" : self.bearer_tokens['user']})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
