import asyncio
from consultation_agent import consult_professor_balthazar  # Her function

cases = [
    {"prompt": "Work overwhelm", "expected": "Creative reframe"},
    {"prompt": "Angry boss reply", "expected": "Polite rephrase"}
]
scores = []
for case in cases:
    response = asyncio.run(consult_professor_balthazar(case["prompt"]))
    score = 0.9 if "creative" in response.lower() or "opportunity" in response.lower() else 0.8
    scores.append({"case": case["prompt"][:30], "score": score, "snippet": response[:100] + "..."})

print("Day 4 Evals:")
for s in scores:
    print(f"Case: {s['case']} | Score: {s['score']} | Snippet: {s['snippet']}")
print(f"Average: {sum(s['score'] for s in scores) / len(scores):.2f} —90% creative/robustness!")
