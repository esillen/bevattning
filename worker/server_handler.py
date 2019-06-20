import requests
import json

SERVER_ADDRESS = "http://rosenhillgarden.pythonanywhere.com"

VALVES = "/valve"
DATA = "/data"


class ServerHandler:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.session.auth = (username, password)

    def send_data(self, data):
        response = self.session.post(SERVER_ADDRESS + DATA, data = data)
        if response.status_code != 200:
            print ("WARNING WARNING COULD NOT SEND DATA TO SERVER")

    def get_valve_states(self):
        response = self.session.get(SERVER_ADDRESS + VALVES)
        if response.status_code != 200:
            print ("WARNING WARNING COULD NOT READ FROM SERVER! VERY UNCOMFORTABLE")
            return False
        else:
            data = response.json()
            valves = data["valves"]
            valves = dict([(item["index"], item["state"]) for item in valves]) # Returns a dict with (index, state) for the valves
            return valves


