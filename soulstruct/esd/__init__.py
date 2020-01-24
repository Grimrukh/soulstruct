from .core import *
from .dark_souls_talk import DarkSoulsTalk


class State(object):

    def previous_states(self):
        pass

    def enter(self):
        pass

    def test(self):
        pass

    def ongoing(self):
        pass

    def exit(self):
        pass
