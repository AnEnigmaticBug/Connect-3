# NISHANT MAHAJAN
# 2017A7PS0112P

from board import P1, P2
from state import ACTION_LIST, State

class Robot:
    def __init__(self, marker):
        if marker not in [P1, P2]:
            raise ValueError('Marker must be one of P1({}) or P2({})'.format(P1, P2))

        self.marker = marker

    def action(self, state):
        action = None

        if self.marker == P1:
            action = state.max_params(-2, +2)[1]
        
        if self.marker == P2:
            action = state.min_params(-2, +2)[1]
        
        return action
