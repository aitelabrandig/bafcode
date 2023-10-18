import logging
import traceback
import sys

# Initialize logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class FrameworkError(Exception):
    """Base exception class for the framework."""
    pass


class ConfigError(FrameworkError):
    """Raised when there's an error related to configurations."""
    pass


class APIError(FrameworkError):
    """Raised when there's an error related to API calls."""
    pass


def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Global exception handler function.

    Args:
    - exc_type (Type[Exception]): The type of the exception.
    - exc_value (Exception): The exception instance.
    - exc_traceback (traceback): The traceback object.
    """
    error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logger.error(error_message)

    # You can add more logic here, e.g., sending notifications, or handling specific types of errors.


# # Set the function `handle_exception` as the global exception handler
# sys.excepthook = handle_exception


# # Example usage:
# if __name__ == "__main__":
#     # This will log the error using the handle_exception function
#     raise ConfigError("This is a test error!")
