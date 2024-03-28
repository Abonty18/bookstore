from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', price={self.price})>"

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, book_id={self.book_id})>"

# Set up logging
logger.add("bookstore.log", rotation="1 week", level="INFO")

# Database setup (replace 'sqlite:///bookstore.db' with your actual database URI)
engine = create_engine('sqlite:///bookstore.db', echo=True)
Session = sessionmaker(bind=engine)

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

# Example usage
if __name__ == "__main__":
    # Debugging logger setup
    logger.debug("Logger setup for models.py started.")
    
    # Creating tables in the database (if not already created)
    Base.metadata.create_all(engine)
    logger.info("Database tables created.")
    
    # Starting a new database session
    session = Session()

    try:
        # Adding example data to the database
        new_user = User(username='john_doe', email='john@example.com')
        session.add(new_user)
        session.commit()
        log_info(f"New user added: {new_user}")
    except Exception as e:
        session.rollback()
        log_error(f"Error adding new user: {e}")
    finally:
        session.close()
    
    logger.debug("Logger setup for models.py completed.")
