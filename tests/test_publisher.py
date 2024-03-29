import unittest
import time
from uphone.publisher import Publisher
from uphone.listener import Listener
from multiprocessing import Process
from multiprocessing import Array


def run_listener(data, n_messages):
    client = Listener('0.0.0.0')

    for i, message in zip(range(n_messages), client):
        data[i] = int(message)


def slowed_range():
    for i in range(10):
        time.sleep(0.01)
        yield str(i).zfill(3)


class TestPublisher(unittest.TestCase):

    def setUp(self):
        self.pub = Publisher()

    def tearDown(self):
        self.pub.close()

    def build_listener(self, n_messages):
        data = Array('d', [0.0]*n_messages)
        client = Process(target=run_listener, args=(data, n_messages))
        client.start()
        return client, data

    def test_sending(self):

        self.pub._send_to_clients('abc')

    def test_distributing_of_generator(self):

        client, data = self.build_listener(5)
        self.pub.send(gen=slowed_range, connection_interval=5)
        client.join()

        self.assertListEqual(
            data[:], [5, 6, 7, 8, 9])

    def test_multiple_check_for_connections(self):

        client, data = self.build_listener(8)
        self.pub.send(gen=slowed_range, connection_interval=2)
        client.join()

        self.assertListEqual(
            data[:], [2, 3, 4, 5, 6, 7, 8, 9])

    def test_client_failover(self):
        # Build client that only fetches two messages
        client, data = self.build_listener(2)
        self.pub.send(gen=slowed_range, connection_interval=3)
        client.join()

        self.assertListEqual(
            data[:], [3, 4])

    def test_server_failover(self):
        # TODO: Test if the server crashes
        pass

    def test_multiple_clients(self):

        self.skipTest(
            'Somehow, this test does not work in Docker instance spawned by Travis '
            'but on pyboard and locally. Do we have deeper design problems somewhere?')

        client_b, data_b = self.build_listener(5)
        client_a, data_a = self.build_listener(2)

        self.pub.send(gen=slowed_range, connection_interval=3)

        for client in [client_a, client_b]:
            client.terminate()
            client.join()

        self.assertListEqual(
            data_a[:], [3.0, 4.0])

        self.assertListEqual(
            data_b[:], [3.0, 4.0, 5.0, 6.0, 7.0])
