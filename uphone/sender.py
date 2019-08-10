"""
Sender class
"""
from uphone.logging import getLogger
from uphone.mic import Mic
import network
from pyb import (
    Pin,
    LED,
)
from uphone.mic import get_data


logger = getLogger(__name__)


class Phone(object):

    def __init__(self, config):
        logger.info('Initialize uPhone')

        self.config = config

        logger.info('Connect to WIFI')
        self.wlan = network.WLAN()

        logger.info('Setup Mic')
        self.mic = Mic(self.config.get_mic_pin())

    def start(self):
        self.connect_to_network()
        self.listen()

    def listen(self):

        while True:
            data = self.mic.get_data(time=1, frequency=10)

            level = self._compute_noise_level(data)
            logger.info('Noise level {}'.format(level))

            # TODO: Make threshold configurable
            if level > 0.3:
                # TODO: Set intensity level
                LED(1).on()
            else:
                LED(1).off()

    def _compute_noise_level(self, data):
        """
        Returns a number between 0 (no noise) and 1 (a lot of noise)
        """
        noise = max(data)
        noise_min = 2600
        noise_max = 4095
        return (noise - noise_min)/(noise_max - noise_min)

    def _set_led_intensity(self, level):
        """
        Set intensity of LED
        """
        pass

    def check_connection(self):
        if not self.wlan.isconnected():
            raise Exception('No WIFI Connection')

    def connect_to_network(self):
        # establish WIFI
        self.wlan.active(1)
        self.wlan.connect(*self.config.get_wifi_credentials())
        self.check_connection()
