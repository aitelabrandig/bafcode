

class ResponderPrompt:
    def generate_final_response(data):
       prompt = """ 
            Please generate an appropriate response based on the provided user data.

            Guidelines:
            1. Restrict your response to information exclusively available within the provided data.
            2. Always validate the integrity and authenticity of the data prior to crafting your response.
            3. Keep in mind that the data is generated by automated agents to assist you in formulating responses. Ensure that you leverage this data optimally in your response.

            Last Emails:
            {data}

           """
       return prompt.format(data=data)

    