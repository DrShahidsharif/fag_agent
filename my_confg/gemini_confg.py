from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from dotenv import load_dotenv

load_dotenv()
import os

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url
)

MODEL = OpenAIChatCompletionsModel(
    model = "gemini-1.5-flash",
    openai_client = client
)