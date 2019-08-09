
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
