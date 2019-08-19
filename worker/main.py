import RPi.GPIO as GPIO
from server_handler import ServerHandler
from threading import Timer
import time
import sched
import json
from hardware_setup import valves, flow_measurers, manual_override, plant_sensor

###############
## CONSTANTS ##
###############
MANUAL_OVERRIDE_UPDATE_INTERVAL = 1
SERVER_UPDATE_INTERVAL = 10 # Updates stuff every 10 seconds
DATA_UPLOAD_INTERVAL = 5 * 60 # Sends data to the server every 5 minutes

#################
## LOCAL FILES ##
#################
# The credentials file should have the following text:
# USERNAME = <your username>
# PASSWORD = <your password>
server_passwords_file = "server_auth.txt"

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


################
## SCHEDULING ##
################

scheduler = sched.scheduler(time.time, time.sleep)

def manual_override_scheduled_update():
    if manual_override.should_override():
        update_valve_states_from_manual_override()
    scheduler.enter(MANUAL_OVERRIDE_UPDATE_INTERVAL, 1, manual_override_scheduled_update)

def server_scheduled_update():
    server.send_healthcheck()
    if not manual_override.should_override():
        update_valve_states_from_server()
    scheduler.enter(SERVER_UPDATE_INTERVAL, 5, server_scheduled_update)

def data_upload_scheduled_update():
    mi_flora_data = plant_sensor.get_latest_data_point_dict()
    update_mi_flora_data_on_server(mi_flora_data)
    scheduler.enter(DATA_UPLOAD_INTERVAL, 10, data_upload_scheduled_update)

###########
## LOGIC ##
###########
plant_sensor.start()

try:
    manual_override_scheduled_update()
    server_scheduled_update()
    data_upload_scheduled_update()
    scheduler.run()
except KeyboardInterrupt:
    plant_sensor.should_run = False
finally:
    GPIO.cleanup()
