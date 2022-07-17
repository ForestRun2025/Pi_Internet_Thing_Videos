import RPi.GPIO as GPIO

# remove before commiting
from RPiSim import GPIO

LED_PIN = 23
SWITCH_PIN = 24

"""Internet 'thing' that can control GPIO on a Raspberry Pi."""


class PiThing(object):

    def __init__(self):
        """Initialize the 'thing'."""
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.setup(SWITCH_PIN, GPIO.IN)

    def read_switch(self):
        """Read the switch state and return its current value."""
        return GPIO.input(SWITCH_PIN)

    def set_led(self, value):
        """Set the LED to the provided value (True = on, False = off)."""
        GPIO.output(LED_PIN, value)
