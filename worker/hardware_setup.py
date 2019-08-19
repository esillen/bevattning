from manual_override import ManualOverride
from solenoid_valve import SolenoidValve
from plant_sensor import PlantSensor
from flow_measurer import FlowMeasurer

###############
## CONSTANTS ##
###############

mi_flora_mac_address = "C4:7C:8D:6A:9F:C6"

###########
## GPIOS ##
###########

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

plant_sensor = PlantSensor(mi_flora_mac_address, poll_interval = 60)

manual_override = ManualOverride(MANUAL_OVERRIDE_MASTER_SWITCH_CHANNEL, MANUAL_OVERRIDE_SWITCH_CHANNELS)
