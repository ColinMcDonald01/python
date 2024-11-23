from television import Television 
import unittest
class MyTestCase(unittest.TestCase):
    def test_power(self):
       self.assertEqual(self.power)
    def test_channel_up(self):
        self.assertAlmostEqual(self.channel_up(True),1)


