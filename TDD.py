"""This file creates a class that encapsulates the functionality of our Raspberry Pi LED contraption

Initialize itself by setting up all the LEDs we need to control.
Provide a led_on() method to turn on individual LEDs
Provide a led_off() method to turn off individual LEDs
Provide a race_up() method to make the leds race up
Provide a race_down() method to make the leds race down
Provide a dance_randomly() method to make the leds dance on and off randomly
Your class should also include tests when the file is run by itself using the if name == "main" trick you've learned.

Katie Brown March 4, 2018"""

#from gpiozero import LED
#from time import sleep

# Naming convention is the CamelCase version of file name
class PiLedContraption:
    _valid_leds = []
    _physical_leds = []

    def __init__(self):
        print("Initializing...")

# Individual LED on
    def led_on(self, led_number):
        print("LED {} is on".format(led_number))

# Individual LED off
    def led_off(self, led_number):
        print("LED {} is off".format(led_number))

 # Setup LEDs

# Test function
if __name__ == "__main__":
    # Testing the initialization
    thingy = PiLedContraption()
    print(type(thingy))
    # Testing turning LEDs on
    thingy.led_on(0)
    print("Test LED on")
    # Testing turning LEDs off
    thingy.led_off(0)
