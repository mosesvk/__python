# Workflow: Why `main.py` Saves Time

This lesson wraps the Anthropic Messages API in a small `ask_claude` helper so you can send prompts from code instead of copying them into a chat UI by hand.

## What the script does

- Loads credentials once (`load_dotenv`) and reuses a single `Anthropic` client.
- Sends user messages with an optional **system** prompt (here, tuned for an accounting firm) and **temperature** to control randomness.
- Runs three experiments: a one-shot definition, repeated low-temperature naming (stable answers), and high-temperature naming (varied answers).

## Why that saves time

| Without automation | With `main.py` |
| --- | --- |
| Open the product UI, paste prompts, copy answers, repeat for A/B tests | One command runs every experiment; output prints in order |
| Easy to forget the system prompt or use inconsistent settings | System message and model settings live in one function |
| Hard to compare “same prompt, different temperature” fairly | Same code path, only `temperature` changes |

You also get a **reusable pattern**: any teammate or CI job can run the same script and get comparable results, which matters when you are validating prompts before production.

## Real-life examples

### 1. Internal Q&A for staff (basic question)

**Scenario:** New hires ask the same policy questions (“What is accounts payable?”) in Slack or email, and a senior accountant answers each time.

**Benefit:** A small internal tool (this pattern + your knowledge base in the system prompt) can draft accurate, on-brand answers in seconds. People still review critical replies, but first drafts and after-hours coverage stop eating senior time.

### 2. Branding and naming with controlled creativity (temperature)

**Scenario:** Marketing needs ten name ideas for an “AI accounting assistant” product. Low temperature gives a shortlist everyone can agree on; high temperature surfaces unexpected options for brainstorming.

**Benefit:** You run the script twice with two temperatures instead of scheduling multiple brainstorming rounds. Stakeholders see **repeatable** low-temp candidates and **diverse** high-temp ideas in one sitting.

### 3. Prompt engineering before you ship

**Scenario:** Before wiring the API into a real app, you need to prove that “accounting firm” tone and guardrails work across dozens of test prompts.

**Benefit:** `ask_claude` becomes your lab bench: change `system_message` or `temperature` in one place, rerun, and diff outputs—much faster than manual chat sessions and easier to turn into regression checks later.

---

**Bottom line:** `main.py` saves time by turning ad-hoc chatting into **scripted, repeatable API calls** with explicit system context and sampling behavior—ideal for training, demos, and prompt iteration inside a firm or product team.
