try:
    import tempfile
except ImportError:
    pass
import os

try:
    import ujson as json
except ImportError:
    import json


class Config(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self._config = json.load(open(filepath, 'r'))

    def get_wifi_credentials(self):
        return self._config["wifi"]["ssid"], self._config["wifi"]["key"]

    def get_mic_pin(self):
        return self._config["mic"]["pin"]


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
