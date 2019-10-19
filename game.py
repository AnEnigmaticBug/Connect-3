# NISHANT MAHAJAN
# 2017A7PS0112P

from board import P1, P2, Board
from robot import Robot
from state import State

class Game:
    def __init__(self):
        self.p1 = Robot(P1)
        self.state = State(Board(4), P1)
        self.turns = 0
    
    def is_over(self):
        winner = self.state.board.check_winner()
        return winner is not None or self.state.board.is_filled()
    
    def p1_turn(self):
        return self.turns % 2 == 0
    
    def advance(self):
        self.turns = self.turns + 1
        self.state = self.state.successor(self.p1.action(self.state))
    
    def make_human_move(self, c):
        self.turns = self.turns + 1
        self.state = self.state.successor(c)