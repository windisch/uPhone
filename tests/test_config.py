import unittest
from uphone.config import (
    Config,
    ConfigWrapper
)


class TestConfig(unittest.TestCase):

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

    def test_wifi(self):

        with ConfigWrapper(self.config) as filepath:
            config = Config(filepath)
            self.assertTupleEqual(
                config.get_wifi_credentials(),
                ('myssid', 'mypw')
            )

    def test_mic_pin(self):
        with ConfigWrapper(self.config) as filepath:
            config = Config(filepath)
            self.assertEqual(config.get_mic_pin(), 'X3')
