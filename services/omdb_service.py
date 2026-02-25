from config import OMDB_API_KEY, OMDB_BASE_URL
import requests


def search_movies(title,year=None):
    params = {
        "apikey" : OMDB_API_KEY,
        "s" : title,
    }
    if year:
        params["y"] = year
    try: 
        response = requests.get(OMDB_BASE_URL,params=params)
        data = response.json()
        if data.get("Response") == "True" :
            return data["Search"],None
        else:
            return [], data["Error"]
    except:
        return [], "No se pudo conectar"
    

def get_movie_detail(imdbID):
        params = {
            "apikey" : OMDB_API_KEY,
            "i" : imdbID,
                }
        try:
            response = requests.get(OMDB_BASE_URL, params=params)
            data = response.json()
            
            if data["Response"] == "True":
                return data,None
            else:
                return None, data["Error"]
        except:
            return  None, "No se pudo conectar"
