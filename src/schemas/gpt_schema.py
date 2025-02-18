from pydantic import BaseModel

class GPTConfigBase(BaseModel):
    name_key: str
    api_key: str
    model_gpt: str

class GPTConfigCreate(BaseModel):
    pass

class GPTConfig(GPTConfigBase):
    id: int

    class Config:
        orm_mode = True