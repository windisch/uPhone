"""
Module with factories for pyboard objects for easier testing.
"""
try:
    from network import WLAN
    from pyb import Timer
    from pyb import Pin
    from pyb import ADC
    from pyb import LED
    from array import array
except ImportError:
    pass


class Board(object):

    def __init__(self):

        self.led = {
            'r':  LED(1),
            'g':  LED(2),
            'b':  LED(3),
        }

        self.wlan = WLAN()

    @staticmethod
    def get_adc_of_pin(pin_name):
        pin = Pin(pin_name, Pin.ANALOG)
        return ADC(pin)

    @staticmethod
    def get_timer(frequency):
        return Timer(8, freq=frequency)

    @staticmethod
    def get_array(length, init_value=0):
        return array('H', (init_value for _ in range(length)))

    def connect_wifi(self, ssid, key):
        # establish WIFI
        self.wlan.active(1)
        self.wlan.connect(ssid, key)

    def is_connected(self):
        return self.wlan.isconnected()

    def turn_off_red_led(self):
        self.led['r'].off()

    def turn_on_red_led(self):
        self.led['r'].on()
