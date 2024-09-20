from openai import OpenAI

class anyscaleHandler:
	def __init__(self, api_key: str, base_url: str = "https://api.endpoints.anyscale.com/v1"):
		"""
		Initialize the AnyScale API handler with the necessary API key and optional base URL.

		:param api_key: Your AnyScale API key.
		:param base_url: The base URL for the AnyScale API endpoints.
		"""
		self.api_key = api_key
		self.base_url = base_url
		self.client = OpenAI(base_url=self.base_url, api_key=self.api_key)

	def anyscale_chat(self, conversation: str, model: str, logprobs: bool = False, top_logprobs: int = None):
		"""
		Handle a chat request for Llama 2, Gemma, Mixtral, and Mistral

		:param conversation: The conversation history as a single string. Includes system instructions.
		:param model: The chat completion model to use.
		:param logprobs: If True, returns the log probabilities of each output token.
		:param top_logprobs: If set, returns the log probabilities of the top top_logprobs tokens at each position.
		:return: The response from the given model.
		"""
		messages = [{"role": "user", "content": conversation}]
		response = self.client.chat.completions.create(
		  model=model,
		  messages=messages,
		  stop=[".","\n"],
		  max_tokens=100,
		  temperature=0.7,
		  logprobs=logprobs,
		  top_logprobs=top_logprobs
		)
		return response.choices[0]
