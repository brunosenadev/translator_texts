from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import AgentGPTCreate, AgentGPTBase, AgentGPT
from functions import update_agent, create_agent, delete_agent, get_agent, get_all_agents
from typing import List

router_agent = APIRouter()

@router_agent.post("/agent/create", response_model=AgentGPT, status_code=201)
def route_create_new_agent(new_agent: AgentGPTCreate, db: Session = Depends(get_db)):
    try:
        new_agent = create_agent(db, new_agent)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao cadastrar um agente novo! Erro: {e}" )
    finally:
        return new_agent
    
@router_agent.get("/agent/{agent_id}", response_model=AgentGPT, status_code=200)
def route_return_agent(agent_id: int, db: Session = Depends(get_db)):
    try:
        agent_founded = get_agent(db, agent_id)

        if not agent_founded:
            raise HTTPException(status_code=404, detail="Agente não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao buscar o agente! Erro: {e}")
    finally:
        return agent_founded
    
@router_agent.put("/agent/{agent_id}", response_model=AgentGPT, status_code=200)
def route_update_agent(agent_id: int, agent_att: AgentGPTBase, db: Session = Depends(get_db)):
    try:
        agent_founded = get_agent(db, agent_id)

        if not agent_founded:
            raise HTTPException(status_code=404, detail="Agente não encontrado.")
        
        agent_updated = update_agent(db, agent_id, agent_att)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao atualizar o agente! Erro: {e}")
    finally:
        return agent_updated
    
@router_agent.delete("/agent/{agent_id}", response_model=AgentGPT, status_code=200)
def route_delete_agent(agent_id: int, db: Session = Depends(get_db)):
    try:
        agent_founded = get_agent(db, agent_id)

        if not agent_founded:
            raise HTTPException(status_code=404, detail="Agente não encontrado.")
        
        agent_deleted = delete_agent(db, agent_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Ocorreu um erro ao deletar o agente! Erro: {e}")
    finally:
        return agent_deleted
    
@router_agent.get("/agent", response_model=List[AgentGPT], status_code=200)
def route_get_all_agents(db: Session = Depends(get_db)):
    try:
        agents_list = get_all_agents(db)

        if len(agents_list) == 0:
            raise HTTPException(status_code=404, detail="Nenhum agente encontrado.")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao buscar os agentes! Erro: {e}")
    finally:
        return agents_list