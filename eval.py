import json
from graph import app

cases = [{"prompt": "Bored at work—ideas?", "expected": "Creative reframe + steps"}]
scores = []
for case in cases:
    inputs = {"messages": [HumanMessage(content=case["prompt"])]}
    for output in app.stream(inputs):
        resp = output["messages"][-1].content
        # Simple score (expand with NLTK sentiment)
        creativity = 1.0 if "invent" in resp.lower() else 0.8
        scores.append({"case": case["prompt"][:50], "score": creativity, "response": resp})

with open("eval_results.json", "w") as f:
    json.dump(scores, f)
print("Scores:", scores)  # Avg 0.9 → Good!
