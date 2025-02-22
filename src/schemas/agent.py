from pydantic import BaseModel, ConfigDict

class AgentGPTBase(BaseModel):
    name_agent: str
    description_agent: str
    rules_agent: str

class AgentGPTCreate(AgentGPTBase):
    pass

class AgentGPT(AgentGPTBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)