"""
Sender class
"""
import logging
import network
from pyb import LED

# logger = logging.getLogger(__name__)


class Phone(object):

    def __init__(self, config):
        self.config = config
        self.wlan = network.WLAN()
        # logger.info('Initialize a sender')

    def start(self):
        self.connect_to_network()

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
