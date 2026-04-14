import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

# Client picks up the key automatically
client = OpenAI()

# Your first real API call
response = client.chat.completions.create(
    model="gpt-4o-mini",       # cheap model, great for learning
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant for an accounting firm."
        },
        {
            "role": "user",
            "content": "In one sentence, what is accounts payable?"
        }
    ]
)

# Pull the response text out
answer = response.choices[0].message.content
print(answer)