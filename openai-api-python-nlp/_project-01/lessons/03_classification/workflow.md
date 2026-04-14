# Workflow: Why `main.py` Saves Time

This lesson uses a `classify` helper that calls the same model with a **strict system prompt** and asks for **JSON-only** replies. That combination is built for **high-volume labeling**: one request can classify many lines of text, and `json.loads` turns the answer into data your app can route on.

## What the script does

- **Sentiment:** Labels customer or internal statements as positive, negative, or neutral.
- **GL account category:** Maps messy transaction descriptions to a fixed chart-of-accounts–style bucket (Revenue, COGS, Travel, etc.).
- **Invoice priority:** Assigns High / Medium / Low urgency from free-text invoice notes.

Temperature defaults to `0` so labels stay stable run to run.

## Why that saves time

| Manual workflow | With `main.py` |
| --- | --- |
| A human reads each item and picks a label | The model labels a **batch** in one API round trip |
| Spreadsheets and opinions drift (“is this Medium or High?”) | The system prompt defines the schema and allowed values |
| Results stay in prose; another step is needed to use them | JSON is ready for dashboards, queues, or databases |

Classification at scale is **O(people)** without automation and **O(API calls)** with it—so 50 items might be one call instead of many minutes of clicking.

## Real-life examples

### 1. Sentiment on support and feedback (Classifier 1)

**Scenario:** After each quarter, finance software support exports hundreds of ticket comments and survey lines. Leadership wants a quick read on morale and product perception.

**Benefit:** Instead of someone skimming every line, the script classifies batches into positive / negative / neutral. Product and CX teams see **trends and outliers** in minutes and only deep-read the sensitive cases.

### 2. GL-style routing from bank or card descriptions (Classifier 2)

**Scenario:** A small business imports raw card transactions (“ADOBE *ACROBAT,” “DELTA AIR,” “AMAZON OFFICE”). Bookkeeping rules require consistent categories for reporting and tax prep.

**Benefit:** Auto-suggested categories cut data-entry time and reduce miscodes. A human still approves exceptions, but **most lines are pre-tagged**, which is the difference between closing books in hours versus days.

### 3. Accounts payable triage (Classifier 3)

**Scenario:** AP receives PDFs and emails: vendor overdue notices, routine net-30 bills, and statutory letters (e.g., IRS). Staff must decide what to pay or escalate first.

**Benefit:** Priority labels let the team **sort work queues** automatically—high-urgency items surface first, routine invoices flow to standard approval. That reduces late fees, missed deadlines, and “everything feels urgent” overload.

---

**Bottom line:** `main.py` saves time by replacing repetitive **read → decide → tag** work with **structured, batch classification** you can plug into real workflows: support analytics, bookkeeping prep, and payment operations.
