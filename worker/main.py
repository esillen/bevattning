import RPi.GPIO as GPIO
from flow_measurer import FlowMeasurer
from solenoid_valve import SolenoidValve
from server_handler import ServerHandler
from threading import Timer
import time

GPIO.setmode(GPIO.BCM) 

#################
## LOCAL FILES ##
#################
# The credentials file should have the following text:
# USERNAME = <your username>
# PASSWORD = <your password>
server_passwords_file = "server_auth.txt"

################
## GPIO SETUP ##
################
FLOW_MEASURER_1_CHANNEL = 2
FLOW_MEASURER_2_CHANNEL = 3

SOLENOID_VALVE_1_CHANNEL = 4
SOLENOID_VALVE_2_CHANNEL = 14
SOLENOID_VALVE_3_CHANNEL = 15
SOLENOID_VALVE_4_CHANNEL = 18

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

#################
## SERVER INIT ##
#################
# Read username and password from file
auth_data = open(server_passwords_file, "r")
auth_lines = auth_data.readlines()
auth_data = [line.split("=") for line in auth_lines]
auth_dict = dict([(item[0].strip(), item[1].strip()) for item in auth_data])
server = ServerHandler(auth_dict["USERNAME"], auth_dict["PASSWORD"])

def update_valve_states_from_server():
    valve_states = server.get_valve_states()
    if valve_states:
        for valve_index in valve_states:
            valves[valve_index].set_state(valve_states[valve_index])
            print (valve_index, valve_states[valve_index])
    else:
        print("Something bad encountered, turning off all valves")
        turn_off_all_valves()

def turn_off_all_valves():
    for valve in valves.values():
        valve.set_state(False)


###########
## LOGIC ##
###########
for i in range(20):

    update_valve_states_from_server()

    time.sleep(1)