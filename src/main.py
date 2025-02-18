from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router_agent, router_gpt
from database import create_tables_and_database
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(router_agent)
app.include_router(router_gpt)

create_tables_and_database()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3500, reload=True)