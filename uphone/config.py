import ujson


class Config(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self._config = ujson.load(open(filepath))

    def get_wifi_credentials(self):
        return self._config["wifi"]["ssid"], self._config["wifi"]["key"]
