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

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

# Logging setup
logger.add("bookstore.log", rotation="1 week", level="INFO")

# Database setup
engine = create_engine('sqlite:///bookstore.db', echo=False)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    logger.info("Application started.")
    
    session = Session()
    try:
        # Add example data here as needed
        new_user = User(username='jane_doe', email='jane@example.com')
        session.add(new_user)
        session.commit()
        logger.info("New user added.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error encountered: {e}")
    finally:
        session.close()
    
    logger.info("Application finished.")
