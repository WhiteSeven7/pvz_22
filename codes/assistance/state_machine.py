from .timing import LoopTiming


class StateMachine:

    def __init__(self, master, state_timing, state):
        self.master = master
        self.state_timing = state_timing
        self.state = state

    def __getitem__(self, item):
        return self.state_timing[item]

    def __setitem__(self, key, value):
        self.state_timing[key] = value

    def __delitem__(self, key):
        del self.state_timing[key]

    def change_state(self, state):
        def end(timing: LoopTiming) -> None:
            timing.user_end()
            state_machine: 'StateMachine' = timing.master
            state_machine.state = state

        self[self.state].user_end = end

    def update(self, time_speed):
        self[self.state].tick(time_speed)
