from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY
from btlewrap.bluepy import BluepyBackend
import datetime
import threading
import time

class PlantSensorDatapoint:
    def __init__(self):
        self.temperature = 0
        self.moisture = 0
        self.light = 0
        self.battery = 0
        self.timestamp = datetime.datetime.utcnow()

    def as_dict(self):
        to_return = {}
        to_return["temperature"] = self.temperature
        to_return["moisture"] = self.moisture
        to_return["light"] = self.light
        #to_return["Conductivity"] = poller.parameter_value(MI_CONDUCTIVITY)
        to_return["battery"] = self.battery
        to_return["timestamp"] = str(self.timestamp)
        return to_return

# yes there are race conditions but whatevz
class PlantSensor(threading.Thread):

    def __init__(self, mac_address, poll_time = 10):
        threading.Thread.__init__(self)
        self.mac_address = mac_address
        self.datapoint = PlantSensorDatapoint()
        self.poll_time = poll_time
        self.should_run = True
        self.lock = threading.Lock()

    def get_latest_data_point_dict(self):
        self.lock.acquire()
        data = self.datapoint.as_dict()
        self.lock.release()
        return data

    def run(self):
        while self.should_run:
            last_time = time.time()
            try:
                self.poll()
            except:
                print('Could not poll mi flora. is it to far away?')
            time.sleep(max(0, self.poll_time - (time.time() - last_time)))

    def poll(self):
        # This is slow but seems to work
        poller = MiFloraPoller(self.mac_address, BluepyBackend)

        self.lock.acquire()
        self.datapoint.temperature = poller.parameter_value(MI_TEMPERATURE)
        self.datapoint.moisture = poller.parameter_value(MI_MOISTURE)
        self.datapoint.light = poller.parameter_value(MI_LIGHT)
        #to_return["Conductivity"] = poller.parameter_value(MI_CONDUCTIVITY)
        self.datapoint.battery = poller.parameter_value(MI_BATTERY)
        self.datapoint.timestamp = datetime.datetime.utcnow()
        self.lock.release()
