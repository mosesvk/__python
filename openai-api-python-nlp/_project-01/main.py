from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

def insert_text(prefix, suffix, context="", temperature=0.7, max_tokens=400):
    """Fill in the middle between a prefix and suffix."""
    system = """You are a professional business writer for an accounting firm.
You will be given a PREFIX (beginning of a document) and a SUFFIX (ending of a document).
Your job is to write ONLY the middle section that connects them naturally.
Do not repeat the prefix or suffix. Just write the middle content."""

    user_content = f"""PREFIX:
{prefix}

SUFFIX:
{suffix}
{f'CONTEXT: {context}' if context else ''}

Write the middle section that connects the prefix to the suffix:"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=max_tokens,
        temperature=temperature,
        system=system,
        messages=[{"role": "user", "content": user_content}]
    )
    return response.content[0].text

# -------------------------------------------------------
# Example 1: From the course — fill in steps
# -------------------------------------------------------
print("=== Fill In: Weight Loss Steps ===")
prefix = "How to lose weight:\n1. Do not skip breakfast."
suffix = "12. Plan your meals."

middle = insert_text(prefix, suffix, temperature=0.7)
print(prefix)
print(middle)
print(suffix)

# -------------------------------------------------------
# Example 2: Accounting firm engagement letter
# -------------------------------------------------------
print("\n=== Fill In: Engagement Letter ===")
prefix = """Dear Mr. Thompson,

We are pleased to confirm our engagement with Thompson Manufacturing, Inc. for the 
fiscal year ending December 31, 2026. This letter outlines the terms of our engagement."""

suffix = """We appreciate the opportunity to serve you and look forward to a productive 
engagement. Please sign and return a copy of this letter to confirm your acceptance.

Sincerely,
[Partner Name]
[Firm Name]"""

context = "Audit engagement, $2.4M revenue client, publicly traded, first-year client"

middle = insert_text(prefix, suffix, context=context, temperature=0.5)
print(prefix)
print("\n" + middle + "\n")
print(suffix)

# -------------------------------------------------------
# Example 3: Audit finding report
# -------------------------------------------------------
print("\n=== Fill In: Audit Finding ===")
prefix = """AUDIT FINDING #3 — Accounts Receivable Reconciliation
Severity: Medium
Date Identified: April 13, 2026

OBSERVATION:"""

suffix = """RECOMMENDATION:
Management should implement a monthly reconciliation procedure with dual review
by the Controller and CFO prior to period close."""

context = "AR balance of $890,000 with $45,000 in unreconciled items over 90 days"

middle = insert_text(prefix, suffix, context=context, temperature=0.3)
print(prefix)
print(middle)
print(suffix)