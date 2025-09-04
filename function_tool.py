from agents import function_tool
from main import FAQS

@function_tool
def answer_faq(question: str) -> str:
    q = question.lower().strip()
    return FAQS.get(q, "Sorry, I don’t know the answer to that question.")