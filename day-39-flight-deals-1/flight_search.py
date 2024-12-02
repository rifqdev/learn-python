import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import random

load_dotenv()

AMADEUS_API = "https://test.api.amadeus.com"

AUTH_ENDPOINT = F"{AMADEUS_API}/v1/security/oauth2/token"
SEARCH_API = f"{AMADEUS_API}/v1/reference-data/locations/cities"
OFFERS_SEARCH_API = f"{AMADEUS_API}/V2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._secret_key = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.city = ""

    def get_iata_code(self, city):
        headers = {"Authorization": f"Bearer {self._token}"}
        parameters = {
            "keyword": city
        }
        response = requests.get(url=SEARCH_API, params=parameters, headers=headers)
        data = response.json()["data"][0]["iataCode"]
        return data
    
    def _get_new_token(self):
        payload = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._secret_key
        }
        
        response = requests.post(url=AUTH_ENDPOINT, data=payload)
        response.raise_for_status()
        return response.json()["access_token"]
    

    def random_future_date(self):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        six_months = today + timedelta(days=180)
        delta_days = (six_months - tomorrow).days
        random_days = random.randint(0, delta_days)
        departured = tomorrow + timedelta(days=random_days)
        returned = tomorrow + timedelta(days=random_days + 10)
        formatted_departured = departured.strftime("%Y-%m-%d")
        formatted_returned = returned.strftime("%Y-%m-%d")
    
        date = {
            "departured": formatted_departured,
            "returned": formatted_returned
        }

        return date


    def find_cheapest_flight(self, destination):
        date = self.random_future_date()

        headers = {"Authorization": f"Bearer {self._token}"}

        parameter = {
            "originLocationCode": "LON",
            "destinationLocationCode": destination,
            "departureDate": "2025-04-1",
            # "returnDate": "2025-04-24",
            "adults": 1,
            "nonStop": True,
            "currencyCode": "GBP"
        }

        # print(parameter)
        response = requests.post(url=OFFERS_SEARCH_API, data=parameter)
        print(response.json())