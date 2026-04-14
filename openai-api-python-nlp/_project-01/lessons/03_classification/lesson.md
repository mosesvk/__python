The Concept
Classification means you give Claude some text and it puts it into a category. No training data needed — just a good prompt. The course uses tweet sentiment as the example, but we're going to make it accounting-relevant.
Two key things this lesson introduces:

Temperature = 0 for classification — you want consistent, not creative
Structured JSON output — instead of a paragraph, get back clean data your code can use

What's new here vs last lesson:

temperature=0 — classification needs deterministic answers, not creativity
json.loads() — parsing the JSON response into a Python dict you can loop over
Prompt engineering — telling Claude exactly what format to respond in

The GL account classifier especially — that's something you could wire into a real expense reporting workflow at your firm. 




While we wait — let's use this time well
Let me explain what the classification code is doing conceptually so when it runs you'll fully understand the output:
The JSON trick is the key insight of this lesson:
python# Instead of Claude responding like this:
"The first tweet is positive, the second is negative..."

# We force it to respond like this:
{"results": [{"text": "...", "sentiment": "positive"}, ...]}

# Which lets us do THIS in Python:
for item in parsed["results"]:
    print(item["sentiment"])  # clean, usable data
This is the difference between a chatbot and a tool. When you get structured JSON back, you can wire it into spreadsheets, databases, email triggers — anything.
For your firm specifically — imagine this running against 500 expense descriptions overnight, automatically tagging each one to the right GL account. That's a real automation.


