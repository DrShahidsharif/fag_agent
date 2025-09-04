from agents import Agent
from my_confg.gemini_confg import MODEL

faq_agent = Agent(
    name="faq_bot",
    model=MODEL,
    instructions="You are a helpful FAQ bot. Answer only based on the predefined FAQs.",
)