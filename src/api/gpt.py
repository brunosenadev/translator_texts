from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import GPTConfigBase, GPTConfigCreate
from models import GPTConfig
from functions import create_user_gpt, get_api_key, get_model_gpt, get_user_gpt, instance_gpt, update_user_gpt, send_message_to_gpt

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
        pass
    except Exception as e:
        pass
    finally:
        pass