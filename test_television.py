import pytest
from television import *


class TestTelevision:

    @classmethod
    def setup_class(cls):
        cls.tv = Television()

    @classmethod
    def teardown_class(cls):
        del cls.tv

    def test_init_initial_state(self):
        assert not self.tv._Television__status
        assert not self.tv._Television__muted
        assert self.tv._Television__volume == Television.MIN_VOLUME
        assert self.tv._Television__channel == Television.MIN_CHANNEL

    def test_power_toggle(self):
        assert not self.tv._Television__status
        self.tv.power()
        assert self.tv._Television__status
        self.tv.power()
        assert not self.tv._Television__status

    def test_mute_toggle(self):
        self.tv.power()
        assert not self.tv._Television__muted
        self.tv.mute()
        assert self.tv._Television__muted
        self.tv.mute()
        assert not self.tv._Television__muted

    def test_channel_up_down(self):
        self.tv.power()  # Ensure TV is powered on
        initial_channel = self.tv._Television__channel

        # Test channel_up()
        self.tv.channel_up()
        new_channel_after_up = self.tv._Television__channel
        assert new_channel_after_up == initial_channel + 1 or new_channel_after_up == Television.MIN_CHANNEL

        # Test channel_down()
        self.tv.channel_down()
        new_channel_after_down = self.tv._Television__channel
        assert new_channel_after_down == initial_channel - 1 or new_channel_after_down == Television.MAX_CHANNEL

        # Assert that after channel_down(), channel returns to initial_channel
        assert new_channel_after_down == initial_channel

    def test_volume_up_down(self):
        self.tv.power()
        initial_volume = self.tv._Television__volume
        self.tv.volume_up()
        assert self.tv._Television__volume == initial_volume + 1
        self.tv.volume_down()
        assert self.tv._Television__volume == initial_volume
