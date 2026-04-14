from dotenv import load_dotenv
from anthropic import Anthropic

# Load the .env file
load_dotenv()

# Client automatically picks up ANTHROPIC_API_KEY from environment
client = Anthropic()

# Your first real API call
response = client.messages.create(
    model="claude-haiku-4-5-20251001",  # fastest + cheapest model, great for learning
    max_tokens=1024,
    system="You are a helpful assistant for an accounting firm.",
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is accounts payable?"
        }
    ]
)

# Pull the response text out
answer = response.content[0].text
print(answer)