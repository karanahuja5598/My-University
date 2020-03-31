from app import app
import unittest

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index_unauth(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        exists = result.data.find("Welcome to the UIC School Notifier, please log in or register.".encode()) != -1
        # assert the response data
        self.assertEqual(exists, True)
    
    def test_login_unauth(self):
        result = self.app.get('/login')
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    def test_register_unauth(self):
        result = self.app.get('/register')
        exists = result.data.find("Register".encode()) != -1
        self.assertEqual(exists, True)

    def test_register_auth(self):
        result = self.app.post('/register', data = {"username" : "agf", "password" : "agf"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    def test_login_auth(self):
        result = self.app.post('/login', data = {"username" : "agf", "password" : "agf"}, follow_redirects=True)
        exists = result.data.find("Welcome to the UIC School Notifier, agf".encode()) != -1
        self.assertEqual(exists, True)

    def test_register_piazza_auth(self):
        pass

    def test_contents_piazza_auth(self):
        pass

    def test_register_gradescope_auth(self):
        pass

    def test_contents_gradescope_auth(self):
        pass

    