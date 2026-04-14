
from dotenv import load_dotenv
from anthropic import Anthropic
import json

load_dotenv()
client = Anthropic()

def classify(system_prompt, user_content, temperature=0):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_content}
        ]
    )
    return response.content[0].text

# --- Classifier 1: Sentiment (from the course) ---
print("=== Sentiment Classifier ===")
system = """Classify the sentiment of each statement as positive, negative, or neutral.
Respond only in JSON format like: {"results": [{"text": "...", "sentiment": "..."}]}"""

statements = [
    "I love how quickly the invoices are processed!",
    "This audit is taking forever and nothing is organized.",
    "The quarterly report has been submitted."
]

user_content = "Classify these:\n" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(statements))
result = classify(system, user_content)
parsed = json.loads(result)
for item in parsed["results"]:
    print(f"  {item['sentiment'].upper()}: {item['text']}")

# --- Classifier 2: GL Account Category ---
print("\n=== GL Account Classifier ===")
system = """You are an accounting expert. Classify each transaction into a GL account category.
Choose from: [Revenue, COGS, Payroll, Rent, Utilities, Travel, Software, Office Supplies, Other]
Respond only in JSON: {"results": [{"transaction": "...", "category": "..."}]}"""

transactions = [
    "Monthly Adobe Acrobat subscription $54.99",
    "Client invoice payment received $12,500",
    "Office printer paper and toner $87.00",
    "Flight to Chicago for client meeting $430"
]

user_content = "\n".join(f"{i+1}. {t}" for i, t in enumerate(transactions))
result = classify(system, user_content)
parsed = json.loads(result)
for item in parsed["results"]:
    print(f"  {item['category']:15} → {item['transaction']}")

# --- Classifier 3: Invoice Priority ---
print("\n=== Invoice Priority Classifier ===")
system = """Classify each invoice description as High, Medium, or Low priority based on urgency.
Respond only in JSON: {"results": [{"invoice": "...", "priority": "..."}]}"""

invoices = [
    "Vendor overdue notice - 90 days past due, $45,000",
    "New vendor first invoice, net 30 terms, $1,200",
    "IRS penalty notice - response required within 10 days"
]

user_content = "\n".join(f"{i+1}. {inv}" for i, inv in enumerate(invoices))
result = classify(system, user_content)
parsed = json.loads(result)
for item in parsed["results"]:
    print(f"  {item['priority']:8} → {item['invoice']}")