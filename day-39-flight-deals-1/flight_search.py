import requests
from dotenv import load_dotenv
import os

load_dotenv()

AMADEUS_API = "https://test.api.amadeus.com"

AUTH_ENDPOINT = F"{AMADEUS_API}/v1/security/oauth2/token"
SEARCH_API = f"{AMADEUS_API}v1/reference-data/locations/cities"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._secret_key = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.city = ""

    def get_iata_code(self, city):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(url=F"{SEARCH_API}?keyword={city}", headers=headers)
        data = response.json()["data"]
        return "TESTING"
    
    def _get_new_token(self):
        payload = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._secret_key
        }
        
        response = requests.post(url=AUTH_ENDPOINT, data=payload)
        response.raise_for_status()
        return response.json()