from pydantic import BaseModel, ConfigDict

class GPTConfigBase(BaseModel):
    name_key: str
    api_key: str
    model_gpt: str

class GPTConfigCreate(GPTConfigBase):
    password: str

class GPTRequest(BaseModel):
    message: str
    model: str

class GPTResponse(BaseModel):
    response: str

class LoginRequest(BaseModel):
    username: str
    password: str

class GPTConfig(GPTConfigBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)