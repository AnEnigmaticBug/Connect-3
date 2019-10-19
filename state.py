# NISHANT MAHAJAN
# 2017A7PS0112P

from board import P1, P2, Board, ColumnFullException

ACTION_LIST = [0, 1, 2, 3]

class State:
    def __init__(self, board, curr_marker):
        self.board = board
        self.curr_marker = curr_marker
    
    def successor(self, action):
        if action not in ACTION_LIST:
            raise ValueError('Unknown action {}'.format(action))

        marker = P1 if self.curr_marker == P2 else P2
        col_no = action

        new_board = self.board.make_copy()
        new_board.make_move(self.curr_marker, col_no)
        return State(new_board, marker)
    
    def utility_value(self):    
        winner = self.board.check_winner()

        if winner == P1:
            return +1 
        if winner == P2:
            return -1
        
        if self.board.is_filled():
            return 0
        
        return None
    

    def min_params(self, α, β, prune = True):
        """
        Give the state's min-value and the action required to get a utility
        value equal to the min-value.

        :param prune: Tells whether to use α-β pruning
        """
        utility = self.utility_value()

        if utility is not None:
            return (utility, None)
        
        v, a = +2, None

        for action in ACTION_LIST:
            if self.board.is_col_empty(action):
                m = self.successor(action).max_params(α, β, prune)[0]

                if m <  v:
                    v, a = m, action
                
                if not prune:
                    continue
                                
                if v <= α:
                    return (v, a)

                β = min(β, v)

        return (v, a)
    
    def max_params(self, α, β, prune = True):
        """
        Give the state's max-value and the action required to get a utility
        value equal to the max-value.

        :param prune: Tells whether to use α-β pruning
        """
        utility = self.utility_value()

        if utility is not None:
            return (utility, None)
        
        v, a = -2, None

        for action in ACTION_LIST:
            if self.board.is_col_empty(action):
                m = self.successor(action).min_params(α, β, prune)[0]

                if m >  v:
                    v, a = m, action
                
                if not prune:
                    continue
                                
                if v >= β:
                    return (v, a)

                α = max(α, v)
                
        return (v, a)
