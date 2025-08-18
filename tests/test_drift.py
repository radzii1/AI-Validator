import json
from .utils import chat, similar

with open("baseline.json") as f:
    BASELINE = json.load(f)

def test_against_baseline():
    failures = []
    for prompt, expected in BASELINE.items():
        res = chat(prompt)
        if not similar(res["reply"], expected):
            failures.append((prompt, expected, res["reply"]))
    assert not failures, f"Drift vs baseline: {failures}"
