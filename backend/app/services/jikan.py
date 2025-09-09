from jikanpy import Jikan
from functools import lru_cache

class AnimeAPI:
    def __init__(self):
        self.jikan=Jikan()
    
    @lru_cache(maxsize=1000)
    def getAnimeDetails(self, animeID:int):

        details=self.jikan.anime(animeID)

        return {
            "id":animeID,
            "title":details.get("data").get("titles")[0].get("title"),
            "year":details.get("data").get("year"),
            "episodes":details.get('data').get('episodes'),
            "type":details.get("data").get("type"),
            "genres":[g.get("name") for g in details.get("data").get("genres",[])],
            "themes":[t.get("name") for t in details.get("data").get("themes",[])],
            "studio":[s.get("name") for s in details.get("data").get("studios",[])],
            "source":details.get("data").get("source"),
            "score":details.get("data").get("score")
        }

    @lru_cache(maxsize=500)
    def searchAnime(self,query:str,num:int=5):
        results=self.jikan.search('anime', query,parameters={"limit":num}).get('data')
        return [
            {
            "id": res.get("mal_id"),
            "title": (res.get("titles") or [{}])[0].get("title")
            }
            for res in results
        ]