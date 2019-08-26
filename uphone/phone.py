"""
Sender class
"""
from uphone.logging import getLogger
from uphone.mic import Mic
from uphone.board import Board
from uphone.publisher import Publisher
from uphone.helpers import zfill

import time

logger = getLogger(__name__)


class Phone(object):

    def __init__(self, config, board=None):
        logger.info('Initialize uPhone')

        self.config = config
        if board is None:
            self.board = Board()
        else:
            self.board = board

        logger.info('Connect to WIFI')
        self.board.connect_wifi(*self.config.get_wifi_credentials())
        logger.info('Setup Mic')
        self.mic = Mic(self.config.get_mic_pin(), board=self.board)
        logger.info('Start publisher')
        self.publisher = Publisher()

    def start(self):

        self.wait_for_wifi()

        logger.info('Start publishing')
        self.publisher.send(self.listen, connection_interval=3)
        self.publisher.close()

    def wait_for_wifi(self):
        while True:
            if self.check_wifi_connection():
                logger.info('WiFi Connected')
                self.board.turn_on_green_led()
                break
            else:
                logger.warning('WiFi not yet connected..wait a bit')
                time.sleep(1)

    def listen(self):

        while True:
            data = self.mic.get_data(time=1, frequency=10)

            level = self._compute_noise_level(data)
            logger.info('Noise level {}'.format(level))

            # TODO: Make threshold configurable
            if level > 40:
                logger.info('Noise detected, call daddy!')
                self.board.turn_off_green_led()
                self.board.turn_on_red_led()
            else:
                self.board.turn_off_red_led()
                self.board.turn_on_green_led()
            yield zfill(str(level), 3)

    def _compute_noise_level(self, data):
        """
        Returns a integer number  between 0 (no noise) and 100 (a lot of noise)
        """
        noise = max(data)
        noise_min = 2600
        noise_max = 4095
        ratio = (noise - noise_min)/(noise_max - noise_min)
        return int(ratio*100)

    def check_wifi_connection(self):
        return self.board.is_connected()
