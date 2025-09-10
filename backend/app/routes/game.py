from fastapi import APIRouter
from app.services.jikan import AnimeAPI
from app.utils.top2000 import get_top2000
import random

router = APIRouter()
anime_api = AnimeAPI()

@router.get("/new")
async def new_game():
    top2000=get_top2000()
    answer_id=random.choice(top2000)
    details=await anime_api.getAnimeDetails(answer_id)
    return details
