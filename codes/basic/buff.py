from ..assistance.fpn import FPN3
from ..assistance.timing import FiniteTiming


class Buff:
    def __init__(self, keeping_time, master=None):
        self.master = master
        self.timing = FiniteTiming(self, keeping_time)


class IceSlow(Buff):
    def __init__(self, master):
        self.name = 'IceSlow'
        super().__init__(FPN3(300), master)

    def begin(self):
        self.master

    def update(self, time_speed):
        self.timing.tick(time_speed)
