# Indicate that 'core' is a package
# Import essential functionalities so they can be accessed directly from the 'core' package

from .error_handler import handle_exception, FrameworkError, ConfigError, APIError
from .logger import setup_logger, framework_logger
from .security import encrypt_data, decrypt_data, hash_data
from .testing_utils import run_tests, mock_api_response


# Initialize any core components if needed
# For example, set the global exception handler or initialize the logger

# Set the global exception handler
import sys
sys.excepthook = handle_exception

# Initialize the logger for the core package
import logging
logger = setup_logger(name="core", log_level=logging.INFO)
