from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome to the Online Bookstore!" in response.data
