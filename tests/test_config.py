import unittest
import tempfile
import os
import json
from uphone.config import Config


class ConfigWrapper(object):
    """
    Wrapper that wraps configurations
    """

    def __init__(self, config):
        self.config = config

    def __enter__(self):

        self.tmpfile = tempfile.NamedTemporaryFile()

        with open(self.tmpfile.name, 'w') as fh:
            fh.writelines(json.dumps(self.config))
        return self.tmpfile.name

    def __exit__(self, exception_type, exception_value, traceback):

        try:
            os.remove(self.tmpfile.name)
        except FileNotFoundError:
            pass


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = {
            'wifi': {
                'key': 'mypw',
                'ssid': 'myssid'
            }
        }

    def test_parsing(self):

        with ConfigWrapper(self.config) as filepath:
            config = Config(filepath)
            self.assertTupleEqual(
                config.get_wifi_credentials(),
                ('myssid', 'mypw')
            )
