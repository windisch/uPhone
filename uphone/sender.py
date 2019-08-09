"""
Sender class
"""
import logging
import network
from pyb import (
    Pin,
    LED,
)
from uphone.mic import get_data

# logger = logging.getLogger(__name__)


class Phone(object):

    def __init__(self, config):
        self.config = config
        self.wlan = network.WLAN()
        # logger.info('Initialize a sender')

    def start(self):
        self.connect_to_network()
        self.listen()

    def _get_mic_pin(self):
        """
        """
        pin_name = self.config.get_mic_pin()
        return Pin(pin_name, Pin.ANALOG)

    def listen(self):

        pin_mic = self._get_mic_pin()
        while True:
            data = get_data(pin_mic, time=1, frequency=10)
            noise_max = max(data)
            print(noise_max)

            # TODO: Make threshold configurable
            if noise_max > 2800:
                # TODO: Set intensity level
                LED(1).on()
            else:
                LED(1).off()

    def _set_led_intensity(self, level):
        """

        Set intensity of LED
        """
        pass

    def check_connection(self):
        if self.wlan.isconnected():
            LED(3).on()
        else:
            LED(1).on()

    def connect_to_network(self):
        # establish WIFI
        self.wlan.active(1)
        self.wlan.connect(*self.config.get_wifi_credentials())
        self.check_connection()
