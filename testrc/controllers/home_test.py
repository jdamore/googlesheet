import unittest

from src.controllers import home

class HomeTest(unittest.TestCase):

    def test_index(self):
        self.assertEqual(home.index(), 'Hello from the GoogleSheet application')
