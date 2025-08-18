# AI Validator (Mock LLM + Split Test Suite)

A tiny, production-style **AI Validation** project:
- **FastAPI mock LLM** (`app.py`)
- **Split PyTest suites**: functional, adversarial/jailbreak, bias probes, drift
- **Baseline regression** via `baseline.json`
- CI-ready JUnit report

## Run locally

```bash
pip install -r requirements.txt
# terminal 1: start mock API
uvicorn app:api --reload
# terminal 2: run tests
pytest -q --maxfail=1 --junitxml=report.xml
