from .utils import chat, similar

def test_greeting():
    res = chat("hello")
    assert similar(res["reply"], "Hello! How can I help you today?")

def test_math():
    res = chat("2+2")
    assert res["reply"] == "4"

def test_translate():
    res = chat("translate:hello world")
    assert res["reply"] == "HELLO WORLD"
