import requests
import json

VALVES = "/valve"
MIFLORA = "/miflora"

class ServerHandler:
    def __init__(self, host, username, password):
        self.host = host
        self.session = requests.Session()
        self.session.auth = (username, password)

    def get_valve_states(self):
        response = self.session.get(self.host + VALVES)
        if response.status_code != 200:
            print ("WARNING WARNING COULD NOT READ FROM SERVER! VERY UNCOMFORTABLE")
            return False
        else:
            data = response.json()
            valves = data["valves"]
            valves = dict([(item["id"], item["state"]) for item in valves]) # Returns a dict with (id, state) for the valves
            return valves

    def update_mi_flora_data(self, data):
        response = self.session.post(self.host + MIFLORA, json = data)
        if response.status_code != 200:
            print ("WARNING WARNING COULD NOT SEND DATA TO SERVER")


