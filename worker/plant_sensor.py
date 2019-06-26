from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from btlewrap.bluepy import BluepyBackend
import datetime


class PlantSensor():

    def __init__(self, mac_address):
        self.mac_address = mac_address

    def poll(self):
        # This is slow but seems to work
        poller = MiFloraPoller(self.mac_address, BluepyBackend)

        to_return = {}
        to_return["temperature"] = poller.parameter_value(MI_TEMPERATURE)
        to_return["moisture"] = poller.parameter_value(MI_MOISTURE)
        to_return["light"] = poller.parameter_value(MI_LIGHT)
        #to_return["Conductivity"] = poller.parameter_value(MI_CONDUCTIVITY)
        to_return["battery"] = poller.parameter_value(MI_BATTERY)
        to_return["timestamp"] = str(datetime.datetime.utcnow())
        return to_return