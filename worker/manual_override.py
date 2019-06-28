import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM) 

class ManualOverride:
    def __init__(self, master_channel, switch_channels_dict):
        self.master_channel = master_channel
        GPIO.setup(self.master_channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.switch_channels_dict = switch_channels_dict
        for channel in switch_channels_dict.values():
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def should_override(self):
        return GPIO.input(self.master_channel)

    def get_channel_states(self):
        return dict([(id, GPIO.input(self.switch_channels_dict[id])) for id in self.switch_channels_dict])

if __name__ == "__main__":
    import time
    manual_override = ManualOverride(17, {1: 27, 2:22, 3:23, 4:24})
    while True:
        print ("Should override{}".format(manual_override.should_override()))
        print ("States: {}".format(manual_override.get_channel_states()))
        time.sleep(1)