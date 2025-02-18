from sqlalchemy.orm import Session
from models import GPTConfig
from schemas import GPTConfigBase, GPTConfigCreate
import openai

def get_api_key(db: Session, id_user: str):
    return db.query(GPTConfig.api_key).filter(GPTConfig.id == id_user).first()

def get_model_gpt(db: Session, id_user: int):
    return db.query(GPTConfig.model_gpt).filter(GPTConfig.id == id_user).first()

def get_user_gpt(db: Session, id_user: int):
    return db.query(GPTConfig).filter(GPTConfig.id == id_user).first()

def create_user_gpt(db: Session, gpt_config: GPTConfigCreate):
    gpt_config_created = GPTConfig(**gpt_config.dict())
    db.add(gpt_config_created)
    db.commit()
    db.refresh(gpt_config_created)

    return gpt_config_created

def update_user_gpt(db: Session, gpt_config_id: int,  gpt_config: GPTConfigBase):
    gpt_config_old = get_user_gpt(db, gpt_config_id)
    update_data = gpt_config.dict(exclude_unset=True)

    for k, v in update_data.items():
        setattr(gpt_config_old, k, v)

    db.commit()
    db.refresh(gpt_config_old)
    return gpt_config_old

def instance_gpt(db: Session, id_user: int):
    openai.api_key = get_api_key(db, id_user)

def send_message_to_gpt(message: str, model: str, agent_rules: str, gpt: openai):
    response = gpt.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": agent_rules },
            {"role": "user", "content": message }
        ]
    )

    response_of_gpt = response['choices'][0]['messages']['content']
    return response_of_gpt


