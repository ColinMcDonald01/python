from television import*
import pytest
class test:
    def setup_method(self):
        self.tv_1 = Television()
    def teardown_method(self):
        del self.tv_1

    def test__innit__(self):
        assert self.channel == self.MIN.CHANNEL
        assert self.__status == False
        assert self.__muted == False
        assert self.__volume == self.MIN_VOLUME
    def test_channel_up(self):
        assert self.tv_1.channel_up(True) == self.channel+1
        assert self.tv_1.channel_up() == self.channel
    def test_channel_down(self):
        assert self.tv_1.channel_down() == self.channel-1
        assert self.tv_1.channel_down() == self.channel
    def test_volume_up(self):
        assert self.tv_1.volume_up() == self.volume+1
        assert self.tv_1.volume_up() == self.volume
    def test_volume_down(self):
        assert self.tv_1.volume_down() == self.volume-1
        assert self.tv_1.volume_down() == self.volume