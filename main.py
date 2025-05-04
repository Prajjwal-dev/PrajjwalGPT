import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize client
genai.configure(api_key=api_key)

def chat_with_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

if __name__ == "__main__":
    print("Welcome to PrajjwalGPT!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        reply = chat_with_gemini(user_input)
        print("Prajjwal:", reply)