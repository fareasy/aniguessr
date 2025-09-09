import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import random

from routes import game,search

app=FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("data/top2000.json") as json_file:
        top2000 = json.load(json_file)

def get_top2000():
    return 

app.include_router(game.router,prefix="/game",tags=["game"])
app.include_router(search.router,prefix="/search",tags=["search"])

@app.get("/")
async def root():
    return{'"message":"hello"'}