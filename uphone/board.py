"""
Module with factories for pyboard objects for easier testing.
"""
try:
    from network import WLAN
    from pyb import Timer
    from pyb import Pin
    from pyb import ADC
    from array import array
except ImportError:
    pass


class Board(object):

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

    @staticmethod
    def get_wifi_connection(ssid, key):
        # establish WIFI
        wlan = WLAN()
        wlan.active(1)
        wlan.connect(ssid, key)
        return wlan
