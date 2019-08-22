"""
Sender class
"""
from uphone.logging import getLogger
from uphone.mic import Mic
from uphone.board import Board
from uphone.publisher import Publisher

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
        self.check_wifi_connection()

        logger.info('Start publishing')
        self.publisher.send(self.listen, connection_interval=3)
        self.publisher.close()

    def listen(self):

        while True:
            data = self.mic.get_data(time=1, frequency=10)

            level = self._compute_noise_level(data)
            logger.info('Noise level {}'.format(level))

            # TODO: Make threshold configurable
            if level > 0.4:
                logger.info('Noise detected, call daddy!')
                self.board.turn_on_red_led()
                # yield "Noise detected, call daddy! (Level={})".format(level)
            else:
                self.board.turn_off_red_led()
                # yield "Everything fine (Level={})".format(level)
            yield level

    def _compute_noise_level(self, data):
        """
        Returns a number between 0 (no noise) and 1 (a lot of noise)
        """
        noise = max(data)
        noise_min = 2600
        noise_max = 4095
        return (noise - noise_min)/(noise_max - noise_min)

    def check_wifi_connection(self):
        if not self.board.is_connected():
            raise Exception('WIFI Connection missing')
