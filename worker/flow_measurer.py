import RPi.GPIO as GPIO  
import time 
import threading

GPIO.setmode(GPIO.BCM) 


class FlowMeasurer:
    def __init__(self, channel):
        self.channel = channel # The GPIO channel for the flow measurer
        self.pulses = 0
        GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.channel, GPIO.RISING, callback = self.on_pulse_up)

    def on_pulse_up(self, info):
        self.pulses += 1
    
    def pop_measurement(self):
        pulses = self.pulses
        self.pulses = 0
        return pulses
