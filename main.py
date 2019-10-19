# NISHANT MAHAJAN
# 2017A7PS0112P

from board import Board, P1, P2
from human import Human
from robot import Robot
from state import State

def play_game():
    p1 = Robot(P1)
    p2 = Human(P2)
    state = State(Board(4), P1)

    while state.utility_value() is None:
        state = state.successor(p1.action(state) if state.curr_marker == P1 else p2.action(state))

        print(state.board)
    
    print('Game Over\n')

while True:
    option = input('->(P)lay\n->(E)xit\n').upper()

    if option == 'P':
        play_game()
    elif option == 'E':
        break
    else:
        print('Please enter either P or E')

print('\nGoodbye')