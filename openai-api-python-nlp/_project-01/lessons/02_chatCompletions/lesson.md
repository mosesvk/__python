The Core Concept
The messages endpoint isn't just for one-off questions. It's designed to handle full conversations and a wide range of NLP tasks:

Generation — brainstorm ideas, write content
Classification — categorize text, sentiment analysis
Transformation — translate, summarize, reformat
Completion — finish incomplete text
Factual responses — answer questions with context

All of these use the exact same client.messages.create() call you already wrote. The only thing that changes is the prompt and parameters.

The Key Parameters to Understand
The course covers these — here's what they mean mapped to Anthropic:
ParameterTypeWhat it doesmodelstringWhich Claude to usemessagesarrayThe conversation historymax_tokensintegerMax length of responsetemperaturefloat 0-1Creativity dial — low=focused, high=randomsystemstringClaude's persona/instructions
Temperature is the big one to understand. Think of it like this:

0.0 → robot, deterministic, same answer every time (good for classification)
0.9 → creative, varied, surprising (good for brainstorming)
0.5 → balanced (good for most tasks)


The function pattern — why it matters
Notice we wrapped the API call in a def ask_claude() function. This is how you'll build real tools — one reusable function that you can call from anywhere. Very JS-like thinking, just Python syntax.
Try it and share what you get back — especially whether you see the temperature difference!


Low temp (0.1) → Both runs recommended almost the same names — Sage, Clarity, Compass, Ledger. Consistent and focused.
High temp (0.9) → More variety — BalanceAI, Atlas, Harmony, Prism showed up. More creative and unpredictable.
That's exactly what the course is teaching. You felt it in real output.