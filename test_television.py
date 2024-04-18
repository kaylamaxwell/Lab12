import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def tearDown(self):
        del self.tv

    def test_init_initial_state(self):
        self.assertFalse(self.tv._Television__status)
        self.assertFalse(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, Television.MIN_VOLUME)
        self.assertEqual(self.tv._Television__channel, Television.MIN_CHANNEL)

    def test_power_toggle(self):
        self.assertFalse(self.tv._Television__status)
        self.tv.power()
        self.assertTrue(self.tv._Television__status)
        self.tv.power()
        self.assertFalse(self.tv._Television__status)

    def test_mute_toggle(self):
        self.tv.power()
        self.assertFalse(self.tv._Television__muted)
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)
        self.tv.mute()
        self.assertFalse(self.tv._Television__muted)

    def test_channel_up_down(self):
        self.tv.power()
        initial_channel = self.tv._Television__channel
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, initial_channel + 1)
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, initial_channel)

    def test_volume_up_down(self):
        self.tv.power()
        initial_volume = self.tv._Television__volume
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, initial_volume + 1)
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, initial_volume)



if __name__ == '__main__':
    unittest.main()
