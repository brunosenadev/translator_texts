from pydantic import BaseModel

class GPTConfigBase(BaseModel):
    name_key: str
    api_key: str
    model_gpt: str

class GPTConfigCreate(BaseModel):
    pass

class GPTRequest(BaseModel):
    message: str
    model: str

class GPTResponse(BaseModel):
    response: str

class GPTConfig(GPTConfigBase):
    id: int

    class Config:
        orm_mode = True