from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from functions import login_user_gpt
from schemas import LoginRequest

router_login = APIRouter()

@router_login.post("/auth/login", status_code=200)
async def login_gpt(data: LoginRequest, db: Session = Depends(get_db)) -> bool:
    loggin_return = login_user_gpt(db, data.username, data.password)

    if loggin_return["user"] and loggin_return["password"]:
        return True
    elif loggin_return["user"] and not loggin_return["password"]:
        raise HTTPException(status_code=400, detail="Senha incorreta!")
    elif not loggin_return["user"] and loggin_return["password"]:
        raise HTTPException(status_code=400, detail="Usuário não encontrado!")
    elif not loggin_return["user"] and not loggin_return["password"]:
        raise HTTPException(status_code=400, detail="Um erro ocorreu ao fazer loggin, favor tentar novamente!")

