import unittest
from unittest.mock import Mock
from unittest.mock import patch

from uphone.config import Config
from uphone.config import ConfigWrapper
from uphone.sender import Phone


class TestSender(unittest.TestCase):

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
        self.board = Mock()

    def test_wifi(self):

        with ConfigWrapper(self.config) as filepath:
            config = Config(filepath)
            Phone(config, board=self.board)
            self.assertTrue(self.board.get_wifi_connection.called)
