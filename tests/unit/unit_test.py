import unittest
from unittest.mock import patch
from app.views import Book, User, Order, Session, engine

class TestViews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the database
        cls.Session = Session
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        # Clean up the database
        cls.session.close()
        engine.dispose()

    def setUp(self):
        # Clear all tables before each test
        self.session.query(Book).delete()
        self.session.query(User).delete()
        self.session.query(Order).delete()
        self.session.commit()

    def tearDown(self):
        # Rollback any uncommitted changes
        self.session.rollback()

    def test_add_user(self):
        # Test adding a new user
        new_user = User(username='test_user', email='test@example.com')
        self.session.add(new_user)
        self.session.commit()

        # Verify that the user was added successfully
        user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    @patch('views.logger')
    def test_logging(self, mock_logger):
        # Test logging functionality
        new_user = User(username='test_user', email='test@example.com')
        self.session.add(new_user)
        self.session.commit()

        # Verify that the logger was called with the expected message
        mock_logger.info.assert_called_with("New user added.")

if __name__ == '__main__':
    unittest.main()
