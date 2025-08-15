from fastapi import FastAPI
from pydantic import BaseModel
from safety_policies import is_blocked, safe_rewrite

api = FastAPI(title="Mock LLM API", version="0.1.0")

class ChatRequest(BaseModel):
    message: str
    system: str | None = None
    temperature: float | None = 0.2

class ChatResponse(BaseModel):
    reply: str
    safety_triggered: bool = False

def toy_llm_logic(msg: str) -> str:
    # simple deterministic behavior so tests are stable
    if msg.strip().lower() in {"hi", "hello"}:
        return "Hello! How can I help you today?"
    if msg.strip().lower() == "2+2":
        return "4"
    if msg.lower().startswith("translate:"):
        return msg.split("translate:",1)[1].strip().upper()
    # default echo with a little formatting
    return f"[ECHO] {msg}"

@api.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if is_blocked(req.message):
        # mimic a compliant refusal + safe rewrite
        return ChatResponse(
            reply=safe_rewrite(req.message),
            safety_triggered=True
        )
    # normal path
    return ChatResponse(reply=toy_llm_logic(req.message))
