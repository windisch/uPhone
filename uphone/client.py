from uphone.listener import Listener
from uphone.logging import getLogger
import socket
import time


logger = getLogger(__name__)


class Client(object):
    """
    """

    def __init__(self, url=None, port=None):
        self.url = url
        self.port = port

        self.listener = Listener(
            url=self.url,
            port=self.port)

    def connect(self):
        logger.info('Try to connect to uPhone')
        for data in self.listener:
            # Analysis
            pass
