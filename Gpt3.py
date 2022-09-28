import openai
from api_key import API_KEY

class BotAI:
    def __init__(self,user_name) -> None:
        openai.api_key = API_KEY
        self.user_name = user_name

    def talk(self,conversation):
        response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(self.user_name + ": ", 1)[0].split("Ava: ", 1)[0]

        return response_str

