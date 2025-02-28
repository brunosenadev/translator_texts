from sqlalchemy.orm import Session
from models import Agent
from schemas import AgentGPTBase, AgentGPTCreate
from base64 import b64decode
from functions.helpers import clean_richtext, text_processing, paragraph_processing

def get_agent(db: Session, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()

def get_agent_rules(db: Session, agent_id: int):
    return db.query(Agent.rules_agent).filter(Agent.id == agent_id).first()[0]

def create_agent(db: Session, agent: AgentGPTCreate):
    agent.rules_agent = b64decode(agent.rules_agent).decode("utf-8")
    agent_created = Agent(**agent.model_dump())
    db.add(agent_created)
    db.commit()
    db.refresh(agent_created)

    return agent_created

def update_agent(db: Session, agent_id: int, agent_updated: AgentGPTBase):
    agent_updated.rules_agent = b64decode(agent_updated.rules_agent).decode("utf-8")
    agent_old = get_agent(db, agent_id)
    update_data = agent_updated.dict(exclude_unset=True)
    
    for k, v in update_data.items():
        setattr(agent_old, k, v)

    db.commit()
    db.refresh(agent_old)

    return agent_old

def delete_agent(db: Session, agent_id: int):
    agent_founded = get_agent(db, agent_id)
    db.delete(agent_founded)
    db.commit()

    return agent_founded

def get_all_agents(db: Session):
    return db.query(Agent).all()