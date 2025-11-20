from app.agent import get_llm_agent


def test_agent_basic_math():
    agent = get_llm_agent()
    result = agent.run("What is 2 + 2? Use the calculator tool.")
    assert "4" in result