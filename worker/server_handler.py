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
        response = None
        try:
            response = self.session.get(self.host + VALVES, timeout = 10)
        except:
            print ("WARNING WARNING COULD NOT READ FROM SERVER! CLIENT SIDE ERROR! VERY UNCOMFORTABLE")
            return False
        if response.status_code != 200:
            print ("WARNING WARNING COULD NOT READ FROM SERVER! BAD RESPONSE CODE FROM SERVER! VERY UNCOMFORTABLE")
            return False
        else:
            data = response.json()
            try:
                valves = data["valves"]
                valves = dict([(item["id"], item["state"]) for item in valves]) # Returns a dict with (id, state) for the valves
            except:
                print ("BAD RESPONSE FROM SERVER! SOMETHING MUST HAVE CHANGED IN THE RESPONSE! VERY UNCOMFORTABLE")
                return False
            return valves

    def update_mi_flora_data(self, data):
        response = None
        try:
            response = self.session.post(self.host + MIFLORA, json = data)
            if response.status_code != 200:
                print ("WARNING WARNING COULD NOT SEND DATA TO SERVER")
        except:
            print ("WARNING WARNING COULD NOT SEND DATA TO SERVER")

