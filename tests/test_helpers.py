import unittest
from uphone.helpers import zfill


class TestHelpers(unittest.TestCase):

    def test_zfill(self):
        self.assertEqual(zfill("3", 3), '003')
        self.assertEqual(zfill("300", 3), '300')
        self.assertEqual(zfill("a", 2), '0a')
