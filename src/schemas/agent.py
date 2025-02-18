from pydantic import BaseModel

class AgentGPTBase(BaseModel):
    name_agent: str
    description_agent: str
    rules_agent: str

class AgentGPTCreate(AgentGPTBase):
    pass

class AgentGPT(AgentGPTBase):
    id: int

    class Config:
        orm_mode = True