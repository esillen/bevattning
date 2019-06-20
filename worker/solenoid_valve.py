import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM) 


class SolenoidValve:
    def __init__(self, channel):
        self.channel = channel
        self.state = False
        GPIO.setup(channel, GPIO.OUT)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
        if self.state:
            GPIO.output(self.channel, GPIO.HIGH)
        else:
            GPIO.output(self.channel, GPIO.LOW)
