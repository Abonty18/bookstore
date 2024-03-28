from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unittest
from models import Book, User, Order
class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up database session
        engine = create_engine('sqlite:///bookstore.db', echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        # Clean up database session
        self.session.close()

    def test_create_order(self):
        # Create a test user and book
        user = User(username='test_user', email='test@example.com')
        book = Book(title='Test Book', author='Test Author', price=20)
        self.session.add_all([user, book])
        self.session.commit()

        # Create an order with the test user and book
        order = Order(user_id=user.id, book_id=book.id)
        self.session.add(order)
        self.session.commit()

        # Retrieve the order from the database and assert its properties
        order_from_db = self.session.query(Order).filter_by(id=order.id).first()
        self.assertIsNotNone(order_from_db)
        self.assertEqual(order_from_db.user_id, user.id)
        self.assertEqual(order_from_db.book_id, book.id)

if __name__ == '__main__':
    unittest.main()
