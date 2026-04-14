from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

def ask_claude(user_message, system_message="You are a helpful assistant for an accounting firm.", temperature=1.0):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        temperature=temperature,
        system=system_message,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.content[0].text

# --- Experiment 1: Basic question ---
print("=== Basic Question ===")
print(ask_claude("In one sentence, what is accounts payable?"))

# --- Experiment 2: Temperature LOW - focused/deterministic ---
print("\n=== Low Temperature (focused) ===")
print(ask_claude("Suggest a name for our AI accounting assistant.", temperature=0.1))
print(ask_claude("Suggest a name for our AI accounting assistant.", temperature=0.1))

# --- Experiment 3: Temperature HIGH - creative/varied ---
print("\n=== High Temperature (creative) ===")
print(ask_claude("Suggest a name for our AI accounting assistant.", temperature=0.9))
print(ask_claude("Suggest a name for our AI accounting assistant.", temperature=0.9))