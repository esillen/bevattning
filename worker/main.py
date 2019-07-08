import RPi.GPIO as GPIO
from flow_measurer import FlowMeasurer
from plant_sensor import PlantSensor
from solenoid_valve import SolenoidValve
from server_handler import ServerHandler
from threading import Timer
from manual_override import ManualOverride
import time
import json

GPIO.setmode(GPIO.BCM) 

#################
## LOCAL FILES ##
#################
# The credentials file should have the following text:
# USERNAME = <your username>
# PASSWORD = <your password>
server_passwords_file = "server_auth.txt"
mi_flora_mac_address_file = "plant_sensor_mac.txt"

################
## GPIO SETUP ##
################
FLOW_MEASURER_1_CHANNEL = 2
FLOW_MEASURER_2_CHANNEL = 3

SOLENOID_VALVE_1_CHANNEL = 4
SOLENOID_VALVE_2_CHANNEL = 14
SOLENOID_VALVE_3_CHANNEL = 15
SOLENOID_VALVE_4_CHANNEL = 18

MANUAL_OVERRIDE_MASTER_SWITCH_CHANNEL = 17
MANUAL_OVERRIDE_SWITCH_CHANNELS = {1:27, 2:22, 3:23, 4:24}

###################
## HARDWARE INIT ##
###################
flow_measurer_1 = FlowMeasurer(FLOW_MEASURER_1_CHANNEL)
flow_measurer_2 = FlowMeasurer(FLOW_MEASURER_2_CHANNEL)

solenoid_valve_1 = SolenoidValve(SOLENOID_VALVE_1_CHANNEL)
solenoid_valve_2 = SolenoidValve(SOLENOID_VALVE_2_CHANNEL)
solenoid_valve_3 = SolenoidValve(SOLENOID_VALVE_3_CHANNEL)
solenoid_valve_4 = SolenoidValve(SOLENOID_VALVE_4_CHANNEL)

flow_measurers = {1:flow_measurer_1, 2:flow_measurer_2}
valves = {1:solenoid_valve_1, 2:solenoid_valve_2, 3:solenoid_valve_3, 4:solenoid_valve_4}

mi_flora_mac_file = open("plant_sensor_mac.txt", 'r')
mi_flora_mac_address = mi_flora_mac_file.readline().strip()
mi_flora_mac_file.close()

plant_sensor = PlantSensor(mi_flora_mac_address)

manual_override = ManualOverride(MANUAL_OVERRIDE_MASTER_SWITCH_CHANNEL, MANUAL_OVERRIDE_SWITCH_CHANNELS)

#################
## SERVER INIT ##
#################
# Read username and password from file
auth_data = open(server_passwords_file, "r")
auth_lines = auth_data.readlines()
auth_data = [line.split("=") for line in auth_lines]
auth_dict = dict([(item[0].strip(), item[1].strip()) for item in auth_data])
server = ServerHandler(auth_dict["HOSTNAME"], auth_dict["USERNAME"], auth_dict["PASSWORD"])

#############
## METHODS ##
#############

def update_valve_states_from_server():
    valve_states = server.get_valve_states()
    if valve_states:
        for valve_id in valve_states:
            valves[valve_id].set_state(valve_states[valve_id])
    else:
        print("Something bad encountered, turning off all valves")
        turn_off_all_valves()

def update_valve_states_from_manual_override():
    valve_states = manual_override.get_channel_states()
    for valve_id in valve_states:
        valves[valve_id].set_state(valve_states[valve_id])

def turn_off_all_valves():
    for valve in valves.values():
        valve.set_state(False)

def poll_mi_flora_data():
    data = None
    try:
        data = plant_sensor.poll()
    except: # happens if the sensor is out of reach
        print ("issue with mi flower. Could be out of reach!")
    return data

def update_mi_flora_data_on_server(mi_flora_data):
    server.update_mi_flora_data(mi_flora_data)

###########
## LOGIC ##
###########
update_interval = 10
plant_sensor.start()
try:
    while True:

        last_update_time = time.time()
        
        # Tells the server that I'm fine
        server.send_healthcheck()

        if manual_override.should_override():
            update_valve_states_from_manual_override()
        else:
            update_valve_states_from_server()

        mi_flora_data = plant_sensor.get_latest_data_point_dict()
        update_mi_flora_data_on_server(mi_flora_data)

        time_to_sleep = max(update_interval - (time.time() - last_update_time), 0)
        print ("Updated at {}, sleeping for {}".format(time.time(), time_to_sleep))
        time.sleep(time_to_sleep)
except KeyboardInterrupt:
    plant_sensor.should_run = False

GPIO.cleanup()