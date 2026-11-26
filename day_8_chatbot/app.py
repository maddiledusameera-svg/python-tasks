from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=api_key)

print("Chatbot is ready! Type 'exit' to quit.")

# Start chat
chat = client.chats.create(model="gemini-3.8-flash")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)

    except Exception as e:
        print("Sorry, Gemini is temporarily unavailable.")
        print("Please try again in a few moments.")