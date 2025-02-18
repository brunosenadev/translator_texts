from sqlalchemy import Column, Integer, String
from database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name_agent = Column(String, nullable=False)
    description_agent = Column(String, nullable=False)
    rules_agent = Column(String, nullable=False)