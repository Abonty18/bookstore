import unittest
from app.models import Book, User, Order

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(title='Test Book', author='Test Author', price=20)
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.price, 20)

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(username='test_user', email='test@example.com')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@example.com')

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        order = Order(user_id=1, book_id=1)
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

if __name__ == '__main__':
    unittest.main()
