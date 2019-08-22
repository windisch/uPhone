import socket
import select
from uphone.logging import getLogger



logger = getLogger(__name__)


class Publisher(object):

    def __init__(self, port=90):

        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Open socket for incoming clients
        self.s.bind(('0.0.0.0', self.port))
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.listen(0)

        self.clients = []
        self.counter = 0

    def connect_new_clients(self):
        self.clients = self.clients + self._get_clients()

    def _get_clients(self):
        """
        s: socket
        """

        print('Check for new clients')
        timeout = 0
        accepted_clients = []
        # Check for two new clients
        # TODO: Here, number of allowed number of clients left should be plugged
        for _ in range(2):
            # TODO: Here may also a repeat work
            sockets_connecting, _, _ = select.select([self.s], [], [], timeout)
            for soc in sockets_connecting:
                client, addr = soc.accept()
                print('client connected from', addr)
                msg = client.recv(1024)
                print('Client MSG {}'.format(msg))
                client.send(b'OK')
                accepted_clients.append(client)

        return accepted_clients

    def send(self, gen, connection_interval=10):
        """
        Publishes a given generator to all connected clients and checks cyclically if new clients
        are connected
        """
        i = 0

        for data in gen():
            logger.info('Send {data} ({i}/{n})'.format(
                data=data,
                i=i,
                n=connection_interval))

            if i == connection_interval:
                self.connect_new_clients()
                i = 0
            else:
                i = i + 1

            self._send_to_clients(data)

    def _send_to_clients(self, data):
        """
        Sends a single data message to all connected clients
        """
        dead_clients = []
        for client in self.clients:
            try:
                client.send(bytes(str(data), 'utf-8'))
            except socket.error:
                logger.warning('Client {} not reachable. Mark him as dead'.format(client))
                dead_clients.append(client)

        for client in dead_clients:
            self.clients.remove(client)

    def close(self):
        self.s.close()