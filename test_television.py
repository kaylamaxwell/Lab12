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
        self.tv.power()
        initial_channel = self.tv._Television__channel
        self.tv.channel_up()
        assert self.tv._Television__channel == initial_channel + 1
        self.tv.channel_down()
        assert self.tv._Television__channel == initial_channel

    def test_volume_up_down(self):
        self.tv.power()
        initial_volume = self.tv._Television__volume
        self.tv.volume_up()
        assert self.tv._Television__volume == initial_volume + 1
        self.tv.volume_down()
        assert self.tv._Television__volume == initial_volume
