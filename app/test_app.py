from app import app
import unittest

# got it from the source mentioned in sources.txt

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

    # check to see if the index page loads the correct message when we aren't logged in
    def test_index_unauth(self):
        result = self.app.get('/')
        exists = result.data.find("Welcome to the UIC School Notifier, please log in or register.".encode()) != -1
        self.assertEqual(exists, True)
    
    # check to see if the login page loads the correct message when we aren't logged in
    def test_login_unauth(self):
        result = self.app.get('/login')
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if the register page loads the correct message when we aren't logged in
    def test_register_unauth(self):
        result = self.app.get('/register')
        exists = result.data.find("Register".encode()) != -1
        self.assertEqual(exists, True)

    # check to see if we can register properly
    def test_register_auth(self):
        result = self.app.post('/register', data = {"username" : "m", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        self.assertEqual(exists, True)

    #check to see if we can register, then log in properly
    def test_register_login_auth(self):
        result = self.app.post('/register', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        result = self.app.post('/login', data = {"username" : "l", "password" : "agfgggg"}, follow_redirects=True)
        exists = result.data.find("Welcome to the UIC School Notifier, l".encode()) != -1
        self.assertEqual(exists, True)

    # check to make sure that you can't register the same username twice
    def test_double_register_auth(self):
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        exists = result.data.find("Sign In".encode()) != -1
        result = self.app.post('/register', data = {"username" : "x", "password" : "agfgghhh"}, follow_redirects=True)
        exists = result.data.find("Username already exists".encode()) != -1
        self.assertEqual(exists, True)


    # check to see if we can update our piazza credentials properly
    def test_register_piazza_auth(self):
        pass

    # check to see if the contents of our piazza account are loaded properly
    def test_contents_piazza_auth(self):
        pass

    # check to see if we can update our gradescope credentials properly
    def test_register_gradescope_auth(self):
        pass

    # check to see if the contents of our gradescope account are loaded properly
    def test_contents_gradescope_auth(self):
        pass

    # check if list of classes loads properly for gradescope, current semester
    def test_className_gradescope_auth(self):
        pass

    