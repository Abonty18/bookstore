from loguru import logger

# Set up logging
logger.add("bookstore.log", rotation="1 week", level="INFO")

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
