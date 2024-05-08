import unittest
from app.models import User, Book, Order, Session, engine

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the database connection and create tables
        cls.session = Session()
        User.metadata.create_all(engine)
        Book.metadata.create_all(engine)
        Order.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        # Close the session and dispose of the engine
        cls.session.close()
        engine.dispose()

    def setUp(self):
        # Clear all tables before each test
        User.metadata.drop_all(engine)
        Book.metadata.drop_all(engine)
        Order.metadata.drop_all(engine)
        User.metadata.create_all(engine)
        Book.metadata.create_all(engine)
        Order.metadata.create_all(engine)

    def tearDown(self):
        # Rollback any uncommitted changes
        self.session.rollback()

    def test_user_creation(self):
        # Test creating a new user
        user = User(username='test_user', email='test@example.com')
        self.session.add(user)
        self.session.commit()

        # Retrieve the user from the database and verify data integrity
        retrieved_user = self.session.query(User).filter_by(username='test_user').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'test@example.com')

    def test_book_creation(self):
        # Test creating a new book
        book = Book(title='Test Book', author='Test Author', price=10)
        self.session.add(book)
        self.session.commit()

        # Retrieve the book from the database and verify data integrity
        retrieved_book = self.session.query(Book).filter_by(title='Test Book').first()
        self.assertIsNotNone(retrieved_book)
        self.assertEqual(retrieved_book.author, 'Test Author')
        self.assertEqual(retrieved_book.price, 10)

    def test_order_creation(self):
        # Test creating a new order
        user = User(username='test_user', email='test@example.com')
        book = Book(title='Test Book', author='Test Author', price=10)
        self.session.add(user)
        self.session.add(book)
        self.session.commit()

        order = Order(user_id=user.id, book_id=book.id)
        self.session.add(order)
        self.session.commit()

        # Retrieve the order from the database and verify data integrity
        retrieved_order = self.session.query(Order).filter_by(user_id=user.id, book_id=book.id).first()
        self.assertIsNotNone(retrieved_order)

if __name__ == '__main__':
    unittest.main()
