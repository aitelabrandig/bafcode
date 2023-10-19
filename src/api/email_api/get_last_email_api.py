import requests
from core import BafLog

EMAIL_API_ENDPOINT = "https://fakerapi.it/api/v1/texts?_quantity=1&_characters=500"  # Placeholder email API endpoint

def get_last_email(user_id):

    logger = BafLog

    if not user_id:
        logger.error("User ID not provided for fetching last email.")
        raise ValueError("User ID is requiread to fetch the last email.")

    # Form the API request
    params = {'user_id': user_id}
    response = requests.get(EMAIL_API_ENDPOINT, params=params)

    # Handle API response
    if response.status_code != 200:
        logger.error(f"Error fetching last email for user {user_id}. API response: {response.text}")
        raise Exception(f"Error fetching last email. API responded with: {response.text}")

    email_data = response.json()
    return email_data
