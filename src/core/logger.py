import logging
import os

# Define log directory and filename
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILENAME = os.path.join(LOG_DIR, 'baf.log')


def setup_logger(name=__name__, log_level=logging.INFO):

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create file handler to log messages to a file
    file_handler = logging.FileHandler(LOG_FILENAME)
    file_handler.setLevel(log_level)

    # Create console handler to print log messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Define log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Use the logger
BafLog = setup_logger()

# # Example usage:
# if __name__ == "__main__":
#     BafLog.info("This is an info message.")
#     BafLog.error("This is an error message.")
