import unittest
import os


BASE_TEST_DIR = os.path.join(os.path.dirname(__file__), '..', 'tests')


def run_tests(test_directory=BASE_TEST_DIR):
    """
    Discover and run tests in the specified directory.

    Args:
    - test_directory (str): Directory where test files are located.

    Returns:
    - unittest.TestResult: Result object detailing test outcomes.
    """
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=test_directory, pattern='*_test.py')
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


def mock_api_response(mock_obj, endpoint, mock_response):
    """
    Mock an API response for testing purposes.

    Args:
    - mock_obj (Mock): The mock object.
    - endpoint (str): API endpoint to mock.
    - mock_response (dict): The mocked response data.

    Returns:
    - None
    """
    mock_obj.get(endpoint, json=mock_response)


# # Example usage:
# if __name__ == "__main__":
#     results = run_tests()
#     print(f"Ran {results.testsRun} tests. Failures: {len(results.failures)}")
