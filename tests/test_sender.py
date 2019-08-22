import unittest
import numpy as np
import time
import itertools
from unittest.mock import Mock

from multiprocessing import Process
from uphone.config import Config
from uphone.config import ConfigWrapper
from uphone.sender import Phone
from uphone.messaging.listener import Listener


def random_noise(random):
    while True:
        yield list(random.normal(
            loc=3000,
            scale=50,
            size=(10, )))


def start_phone(config, board):
    """
    Helper method that starts a uPhone
    """
    with ConfigWrapper(config) as filepath:
        config = Config(filepath)
        p = Phone(config, board=board)
        p.start()


class TestSender(unittest.TestCase):

    def get_phone_process(self):
        phone_process = Process(
            target=start_phone,
            args=(self.config, self.board))
        return phone_process

    def setUp(self):
        self.config = {
            'wifi': {
                'key': 'mypw',
                'ssid': 'myssid'
            },
            'mic': {
                'pin': 'X3'
            }
        }
        random = np.random.RandomState(100)

        self.board = Mock()
        self.board.get_array = Mock(side_effect=random_noise(random))

    def test_wifi(self):

        with ConfigWrapper(self.config) as filepath:
            config = Config(filepath)
            Phone(config, board=self.board)
            self.assertTrue(self.board.connect_wifi.called)

    def test_sending(self):
        phone_process = self.get_phone_process()

        # Give the phone a bit time to start up
        phone_process.start()
        time.sleep(0.1)
        client = Listener('0.0.0.0', 90)
        data = [d for d in itertools.islice(client, 10)]
        phone_process.terminate()
        phone_process.join()

        self.assertEqual(len(data), 10)
