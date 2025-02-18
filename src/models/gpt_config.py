from sqlalchemy import Column, Integer, String
from database import Base

class GPTConfig(Base):
    __tablename__ = "gpt_config"

    id = Column(Integer, primary_key=True, index=True)
    name_key = Column(Integer, nullable=True)
    api_key = Column(String, nullable=False, unique=True)
    model_gpt = Column(String, nullable=False)