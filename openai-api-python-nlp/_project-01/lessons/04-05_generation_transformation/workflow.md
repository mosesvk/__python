# Workflow: Why `main.py` Saves Time

This lesson uses a single `generate` helper around the Anthropic Messages API. The **logic** is the same for every task: set a **system** role (who the model is), pass **user** content (what to do), then tune **`temperature`** and **`max_tokens`** for either **open-ended creation** (generation) or **structured rewriting** (transformation).

## What the script does

### Shared pattern

- Loads the API key once (`load_dotenv`) and reuses one `Anthropic` client.
- `generate(system_prompt, user_content, temperature=0.75, max_tokens=400)` keeps all calls consistent; you only change prompts and knobs per use case.

### Part 1: Generation (create new text or code)

| Experiment | Role | Typical temperature |
| --- | --- | --- |
| Brainstorm AI + accounting ideas | Creative consultant | Higher (`0.75`) for variety |
| Draft a client email (Q1 return, deadline, call) | Professional CPA | Medium (`0.5`) for tone + reliability |
| Write a Python helper (totals, average, count) | Python expert | Lower (`0.2`) for correctness |

### Part 2: Transformation (reshape existing input)

| Experiment | Role | Typical temperature |
| --- | --- | --- |
| Summarize long meeting notes to bullets | Executive assistant | Low–medium (`0.3`) |
| Convert messy lines to **CSV only** | Data formatter | Very low (`0.1`) for deterministic structure |
| Rewrite formal/legal text as plain English | Plain-language rewriter | Low–medium (`0.3`) |

**Logic:** Higher temperature when you want **ideas and phrasing** to vary; lower temperature when you want **facts, format, or code** to stay tight and repeatable.

## Why that saves time

| Without automation | With `main.py` |
| --- | --- |
| Switch between chat, email, and IDE to produce drafts and snippets | One script runs every scenario in sequence with explicit system prompts |
| Reformat messy exports by hand in spreadsheets | Model outputs CSV-shaped text from unstructured lines (then you paste or pipe onward) |
| Senior staff write every summary and every client email from a blank page | Model produces a **first pass**; people edit for policy and judgment |
| Inconsistent tone across channels | Each call locks behavior in `system_prompt` |

## Real-life examples

### Generation

1. **Brainstorming** — A managing partner wants concrete AI use cases before a partner retreat. The model lists options fast so the meeting spends time on **prioritization**, not blank-page brainstorming.

2. **Client email draft** — Tax season brings hundreds of “your return is ready” messages. A templated prompt plus client-specific facts yields drafts that staff **review and send**, cutting composition time without removing human sign-off.

3. **Small code snippets** — An analyst needs a utility (e.g., invoice list → total, average, count). Generated code is a **starting point** to paste into a notebook or script; a developer still validates edge cases and tests.

### Transformation

4. **Summarize** — Audit committee or board notes arrive as long paragraphs. Bullet summaries help executives and file prep **without** rereading full minutes for every stakeholder.

5. **Reformat to CSV** — AR aging or vendor lists arrive as inconsistent text from email or PDF paste. Structured CSV (even as an intermediate) speeds **import into Excel, databases, or downstream tools**.

6. **Plain English** — Clients misunderstand formal engagement letters or IRS-style language. A simplified rewrite improves **comprehension and response rates**; legal still approves anything binding.

---

**Bottom line:** `main.py` saves time by separating **creation** (generation, tuned for creativity or code) from **editing** (transformation, tuned for fidelity and format)—all through one reusable function and explicit temperatures per task.
