from ...api import get_last_email
from core import framework_logger

class GetLastEmail:
    def __init__(self):
        self.logger = framework_logger

    def execute(self, data):
        """
        Fetch the last email for the provided user.

        Args:
        - data (dict): Contains user-specific data, such as user_id.

        Returns:
        - dict: Response data containing the last email details.
        """
        user_id = data['user_id']
        if not user_id:
            self.logger.error("User ID not provided for GetLastEmail command.")
            raise ValueError("User ID is required to fetch the last email.")

        email_data = get_last_email(user_id)
        return email_data
