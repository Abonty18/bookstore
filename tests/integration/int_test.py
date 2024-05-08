import unittest
from unittest.mock import patch
from flask import Flask
from app.views import app, User, Session, engine

class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client
        cls.app = app.test_client()
        cls.app_context = app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        # Pop the Flask app context
        cls.app_context.pop()

    def setUp(self):
        # Set up the database connection
        self.Session = Session
        self.session = self.Session()

    def tearDown(self):
        # Rollback any uncommitted changes
        self.session.rollback()

    def test_user_registration(self):
        # Test user registration endpoint
        response = self.app.post('/register', json={'username': 'test_user', 'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)

        # Verify that the user was added to the database
        user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main()
