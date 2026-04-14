from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

def generate(system_prompt, user_content, temperature=0.75, max_tokens=400):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_content}
        ]
    )
    return response.content[0].text

# ============================================================
# PART 1: GENERATION
# ============================================================

# --- Generation 1: Brainstorming (from the course) ---
print("=== Brainstorm: AI + Accounting Ideas ===")
result = generate(
    system_prompt="You are a creative technology consultant for accounting firms.",
    user_content="Brainstorm 3 practical ways AI could save time at a top 25 accounting firm. Be specific and concise.",
    temperature=0.75
)
print(result)

# --- Generation 2: Draft a client email ---
print("\n=== Generate: Client Email Draft ===")
result = generate(
    system_prompt="You are a professional CPA at a top accounting firm. Write concise, professional emails.",
    user_content="""Draft a short email to a client letting them know:
- Their Q1 tax return is ready for review
- We need their signature by April 25th
- They can schedule a 15-min call to review
Client name: Robert Chen""",
    temperature=0.5
)
print(result)

# --- Generation 3: Generate Python code ---
print("\n=== Generate: Python Code ===")
result = generate(
    system_prompt="You are a Python expert. Write clean, commented code.",
    user_content="Write a Python function that takes a list of invoice amounts and returns the total, average, and count.",
    temperature=0.2
)
print(result)

# ============================================================
# PART 2: TRANSFORMATION
# ============================================================

# --- Transformation 1: Summarize ---
print("\n=== Transform: Summarize ===")
long_text = """
The audit committee met on March 15th to review Q4 financials. Revenue was up 12% 
year over year, driven primarily by new client acquisitions in the healthcare sector. 
Operating expenses increased by 8% due to expanded headcount and office lease renewals 
in three locations. EBITDA margin improved slightly to 23.4% from 22.1% the prior year. 
The committee flagged three open items: reconciliation of intercompany transactions, 
pending resolution of a vendor dispute totaling $340,000, and completion of the fixed 
asset depreciation schedule. Next meeting is scheduled for April 20th.
"""
result = generate(
    system_prompt="You are an executive assistant. Summarize meeting notes into bullet points.",
    user_content=f"Summarize this into 3 bullet points:\n{long_text}",
    temperature=0.3
)
print(result)

# --- Transformation 2: Reformat data ---
print("\n=== Transform: Reformat to CSV ===")
messy_data = """
John Smith owes $4,500 due March 1st
ABC Corp invoice $12,000 due February 15th  
Sarah Johnson balance $890 due March 30th
XYZ LLC outstanding $67,400 due January 31st
"""
result = generate(
    system_prompt="You are a data formatter. Convert input into clean CSV format only. No explanation.",
    user_content=f"Convert to CSV with columns: name, amount, due_date:\n{messy_data}",
    temperature=0.1
)
print(result)

# --- Transformation 3: Translate tone ---
print("\n=== Transform: Formal → Simple ===")
formal_text = "Pursuant to our engagement letter dated January 1st, we hereby notify you that the aforementioned reconciliation discrepancies remain unresolved and require your immediate attention."
result = generate(
    system_prompt="Rewrite accounting/legal text in plain, simple English that anyone can understand.",
    user_content=f"Simplify this: {formal_text}",
    temperature=0.3
)
print(result)