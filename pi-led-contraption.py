"""This file creates a class that encapsulates the functionality of our Raspberry Pi LED contraption

Initialize itself by setting up all the LEDs we need to control.
Provide a led_on() method to turn on individual LEDs
Provide a led_off() method to turn off individual LEDs
Provide a race_up() method to make the leds race up
Provide a race_down() method to make the leds race down
Provide a dance_randomly() method to make the leds dance on and off randomly
Your class should also include tests when the file is run by itself using the if name == "main" trick you've learned.

Katie Brown March 4, 2018"""


# Define a sleeptime
st = 0.5

from gpiozero import LED
from time import sleep

# Naming convention is the CamelCase version of file name
class PiLedContraption:
    _led = []
    _valid_leds = []
    _physical_leds = []

    def __init__(self):
        print("Initializing...")
        # Setup LEDs
        self._valid_leds = [18, 19, 20, 21, 22]
        for i in self._valid_leds:
            # LED(i) is the pin number
            self._physical_leds.append(LED(i))
            #self._physical_leds.append(i)

# Individual LED on
    def led_on(self, led_number):
        if 0 <= led_number > 5:
            print("Invalid LED number {}".format(led_number))
        else:
            print("LED {} is on".format(led_number))
            self._physical_leds[led_number].on()
            #self._physical_leds[led_number] = 1


# Individual LED off
    def led_off(self, led_number):
        if 0 <= led_number > 5:
            print("Invalid LED number {}".format(led_number))
        else:
            print("LED {} is off".format(led_number))
            self._physical_leds[led_number].off()
            #self._physical_leds[led_number] = 0


if __name__ == "__main__":

    # Testing the initialization
    thingy = PiLedContraption()
    print(type(thingy))

    # Testing turning LEDs on
    thingy.led_on(0)
    sleep(st)
    print("Test LED on")
    # Testing LED number validation
    thingy.led_on(99)
    sleep(st)
    # Testing turning LEDs off
    thingy.led_off(0)
    sleep(st)
    print("Test LED off")# Test function

    # Test visible on Raspberry Pi
    thingy.led_on(0)
    sleep(st)
    thingy.led_on(1)
    sleep(st)
    thingy.led_on(2)
    sleep(st)
    thingy.led_off(1)
    sleep(st)