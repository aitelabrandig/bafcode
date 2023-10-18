

class LastEmailsPrompt:
    def get_last_emails(data):
      prompt = """ 
         Please provide a concise summary of the most recent emails from the user's inbox.

            Instructions:
            1. Ensure the confidentiality and privacy of the user's data at all times.
            2. Summarize each email without compromising the essence of its content.
            3. Prioritize relevance and brevity in your summaries.
            4. Limit your response to the information present in the provided data.

            Email Data:
            {data}


           """
      
      return prompt.format(data=data)


    