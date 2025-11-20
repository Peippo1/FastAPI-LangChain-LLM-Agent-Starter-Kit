from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agent import get_llm_agent
from app.schemas import AgentRequest, AgentResponse
from app.config import get_settings

settings = get_settings()
app = FastAPI(
    title="LLM Agent Starter Kit",
    version="0.1.0",
    description="FastAPI + LangChain sync agent starter template.",
)

# Basic CORS (can be tightened by end user)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": settings.environment,
    }


@app.post("/agent/invoke", response_model=AgentResponse)
def invoke_agent(payload: AgentRequest):
    """
    Invoke the LangChain agent with a simple text input.
    """
    agent = get_llm_agent()
    result = agent.run(payload.input)
    return AgentResponse(output=result)