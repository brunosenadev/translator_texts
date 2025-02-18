from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import GPTConfigBase, GPTConfigCreate, GPTRequest, GPTResponse
from models import GPTConfig
from functions import create_user_gpt, get_user_gpt, update_user_gpt, delete_user_gpt, send_message_to_gpt, instance_gpt, get_agent_rules

router_gpt = APIRouter()

@router_gpt.post("/gptconfig/create", response_model=GPTConfig, status_code=201)
def route_create_new_gpt_config(gpt_config: GPTConfigCreate, db: Session = Depends(get_db)): 
    try:
        new_gpt_config = create_user_gpt(db, gpt_config)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao adicionar um novo usuário! Erro: {e}")
    finally:
        return new_gpt_config
    
@router_gpt.get("gptconfig/{user_gpt_id}", response_model=GPTConfig, status_code=200)
def route_return_gpt_config(user_gpt_id: int, db: Session = Depends(get_db)):
    try:
        gpt_config_founded = get_user_gpt(db, user_gpt_id)

        if not gpt_config_founded:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao buscar o usuário! Erro: {e}")
    finally:
        return gpt_config_founded
    
@router_gpt.put("gptconfig/{user_gpt_id}", response_model=GPTConfig, status_code=200)
def route_update_gpt_config(user_gpt_id: int, user_gpt: GPTConfigBase, db: Session = Depends(get_db)):
    try:
        gpt_config_founded = get_user_gpt(db, user_gpt_id)

        if not gpt_config_founded:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        gpt_config_updated = update_user_gpt(db, user_gpt_id, user_gpt)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao atualizar o usuário! Erro: {e}")
    finally:
        return gpt_config_updated

@router_gpt.delete("/gptconfig/{user_gpt_id}", response_model=GPTConfig, status_code=200)
def route_delete_gpt_config(user_gpt_id: int, db: Session = Depends(get_db)):
    try:
        gpt_config_founded = get_user_gpt(db, user_gpt_id)

        if not gpt_config_founded:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        gpt_config_deleted = delete_user_gpt(db, gpt_config_founded)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ocorreu um erro ao deletar o usuário! Erro: {e}")
    finally:
        return gpt_config_deleted
    
@router_gpt.post("/gpt_chat/send_message", response_model=GPTResponse)
def route_send_message(request: GPTRequest, user_id: int, db: Session = Depends(get_db)):
    try:
        openai = instance_gpt(db, user_id)
        agent_rules = get_agent_rules(db, user_id)
        gpt_response = send_message_to_gpt(request.message, request.model, agent_rules, openai)
        return GPTResponse(response=gpt_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao se comunicar com o GPT: {e}")