from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest
from models import Book, User # Replace 'your_module_name' with the actual name of your module

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Set up database session
        engine = create_engine('sqlite:///bookstore.db', echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        # Clean up database session
        self.session.close()

    def test_user_creation(self):
        new_user = User(username='test_user', email='test@example.com')
        self.session.add(new_user)
        self.session.commit()
        user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

    def test_add_book(self):
        new_book = Book(title='Test Book', author='Test Author', price=20)
        self.session.add(new_book)
        self.session.commit()
        book = self.session.query(Book).filter_by(title='Test Book').first()
        self.assertIsNotNone(book)
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.price, 20)

if __name__ == '__main__':
    unittest.main()
