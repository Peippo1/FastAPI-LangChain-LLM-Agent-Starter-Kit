from pydantic import BaseModel


class AgentRequest(BaseModel):
    input: str


class AgentResponse(BaseModel):
    output: str