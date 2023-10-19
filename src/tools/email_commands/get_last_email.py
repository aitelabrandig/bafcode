from api import get_last_email
from core import BafLog
from prompts import LastEmailsPrompt
class GetLastEmail:
    def __init__(self):
        self.logger = BafLog

    def execute(self, data):
        user_id = data['user_id']
        if not user_id:
            self.logger.error("User ID not provided for GetLastEmail command.")
            raise ValueError("User ID is required to fetch the last email.")

        emails = get_last_email(user_id)
        prompt = LastEmailsPrompt.get_last_emails(emails)
        return prompt
