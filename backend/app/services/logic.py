from services.jikan import AnimeAPI

animeapi=AnimeAPI()

#check guesses

def check_guess(answer,guess):
    correct=answer.get("id")==guess.get("id")
    if correct:
        return {
            "correct":True,
            "status":"won",
        }
    else:
        return {
            "correct":False,
            "status":"playing",
            "details":{
                "year":{
                    "value":guess.get("year"),
                    "status":"higher" if guess
                },
                "episodes",
                "type",
                "genres":[g.get("name") for g in details.get("data").get("genres",[])],
                "themes":[t.get("name") for t in details.get("data").get("themes",[])],
                "studio":[s.get("name") for s in details.get("data").get("studios",[])],
                "source":details.get("data").get("source"),
                "score":details.get("data").get("score")
            }
        }