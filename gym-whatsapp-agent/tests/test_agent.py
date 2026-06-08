from app.agent.llm import LLM

def test_llm_echo():
    llm = LLM()
    out = llm.generate("hello")
    assert "Echo" in out.get("response")
