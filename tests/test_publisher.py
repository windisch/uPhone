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
        yield i


class TestPublisher(unittest.TestCase):

    def setUp(self):
        self.pub = Publisher()

    def tearDown(self):
        self.pub.close()

    def build_listener(self, n_messages):
        data = Array('i', [0]*n_messages)
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
        client_a, data_a = self.build_listener(2)
        client_b, data_b = self.build_listener(5)
        self.pub.send(gen=slowed_range, connection_interval=3)
        client_a.join()
        client_b.join()
        self.assertListEqual(
            data_a[:], [3, 4])

        self.assertListEqual(
            data_b[:], [3, 4, 5, 6, 7])
