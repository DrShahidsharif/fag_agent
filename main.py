import asyncio
from agents import Runner
from agents import set_tracing_disabled
from my_agent.my_agent import faq_agent
set_tracing_disabled(True)

FAQS = {
    "what is your name?": "I am a simple FAQ bot.",
    "who created you?": "I was created for preparing an assignment using the OpenAI Agent SDK.",
    "what can you do?": "I can answer some basic questions.",
    "how are you?": "I am just a bot, but I am doing great!",
    "bye": "Goodbye! Have a nice day."
}

async def main():
    print("FAQ Bot is running! Ask me something (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        
        result = await Runner.run(faq_agent, input=user_input, )
        print("Bot:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())