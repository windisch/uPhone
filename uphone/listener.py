import socket
import time
from uphone.logging import getLogger


logger = getLogger(__name__)


class Listener(object):

    def __init__(self, url, port=9999):

        self.url = url
        self.port = port

    def __iter__(self, n_messages=-1):
        with socket.socket() as socket_uphone:
            logger.info('Connect to uphone')
            socket_uphone.connect((self.url, self.port))
            # Tell server to send data to sockt
            socket_uphone.send(b'Hi uPhone, please gimme data')
            result = socket_uphone.recv(2)

            logger.info('Got {} from server'.format(result))
            if result != b'OK':
                raise Exception('Something went wrong')
            while True:
                data = socket_uphone.recv(1024)
                if data:
                    yield float(data.decode("utf-8"))
                else:
                    break
