import openai
class openaiHandler:
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI API handler with the necessary API key.
        
        :param api_key: Your OpenAI API key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def gpt_chat(self, conversation: str, model: str) -> str:
        """
        Handle a chat requests for GPT-3.5 and GPT-4.
        
        :param conversation: The conversation history as a single string. Includes system instructions.
        :param model: The chat completion model to use.
        :return: The response from GPT3.5 or GPT-4.
        """
        messages = [{"role": "user", "content": conversation}]
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            stop=[".","\n"],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content
