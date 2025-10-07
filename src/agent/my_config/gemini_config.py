from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

gemni_client = AsyncOpenAI(
    api_key= key, 
    base_url= base_url
)

MODEL = OpenAIChatCompletionsModel(model = "gemini-2.5-flash", openai_client = gemni_client)
