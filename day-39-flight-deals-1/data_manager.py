import requests
from dotenv import load_dotenv
import os

load_dotenv()

API = os.getenv("API_SHEET")
AUTH = (os.getenv("USERNAME"), os.getenv("PASSWORD"))

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_data()

    def get_data(self):
        response = requests.get(url=API, auth=AUTH)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_iata(self, payload, id):
        response = requests.put(url=f"{API}/{id}", json=payload)
        print(response.text)