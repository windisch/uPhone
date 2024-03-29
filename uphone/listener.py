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
            logger.info('Connect to uphone at {url}:{port}'.format(
                url=self.url,
                port=self.port)
            )
            socket_uphone.connect((self.url, self.port))
            # Tell server to send data to sockt
            socket_uphone.send(b'Hi uPhone, please gimme some noise')
            result = socket_uphone.recv(2)

            logger.info('Received {} from Phone'.format(result))
            if result != b'OK':
                raise Exception('Could not connect')
            while True:
                data = socket_uphone.recv(3).decode('utf-8')
                logger.info('Received {}'.format(data))
                if data:
                    yield int(data)
                else:
                    break
