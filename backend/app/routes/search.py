from fastapi import APIRouter,Query
from app.services.jikan import AnimeAPI

router = APIRouter()
anime_api=AnimeAPI()

@router.get("/search/")
def search_anime(query:str=Query(min_length=2),lim:int=5):
    results= anime_api.searchAnime(query,lim)
    return results