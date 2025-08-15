BLOCK_KEYWORDS = {
    "how to make a bomb",
    "bypass paywall",
    "credit card generator",
    "child sexual",
    "kill yourself",
    "terrorist",
    "jailbreak:",
    "ignore all previous instructions",
    "act as evilgpt",
}

BIAS_PROBES = {
    "doctor": {"unwanted_association": "male"},
    "nurse": {"unwanted_association": "female"},
}

def is_blocked(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in BLOCK_KEYWORDS)

def safe_rewrite(original: str) -> str:
    return ("I can’t help with that request. "
            "Here’s a safer alternative: consider legal, ethical learning resources.")
