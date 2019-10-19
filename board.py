# NISHANT MAHAJAN
# 2017A7PS0112P

EMPTY = 0
P1 = 1
P2 = 2

class ColumnFullException(Exception):
    def __str__(self):
        return 'Column had no space for making a move'

class Board:
    def __init__(self, side):
        self.side = side
        self.grid = [[EMPTY for c in range(side)] for r in range(side)]
    
    def is_col_empty(self, c):
        for r in range(0, self.side):
            if self.grid[r][c] == EMPTY:
                return True
        
        return False
    
    def check_winner(self):
        for r in range(self.side):
            for c in range(self.side):
                if self.grid[r][c] == EMPTY:
                    continue

                not_at_vt_edge = r != 0 and r != self.side - 1
                not_at_hz_edge = c != 0 and c != self.side - 1

                if not_at_vt_edge:
                    if self.grid[r - 1][c] == self.grid[r][c] == self.grid[r + 1][c]:
                        return self.grid[r][c]
                
                if not_at_hz_edge:
                    if self.grid[r][c - 1] == self.grid[r][c] == self.grid[r][c + 1]:
                        return self.grid[r][c]
                
                if not_at_vt_edge and not_at_hz_edge:
                    if self.grid[r - 1][c - 1] == self.grid[r][c] == self.grid[r + 1][c + 1]:
                        return self.grid[r][c]
                    if self.grid[r + 1][c - 1] == self.grid[r][c] == self.grid[r - 1][c + 1]:
                        return self.grid[r][c]
        return None
    
    def is_filled(self):
        for r in range(self.side):
            if EMPTY in self.grid[r]:
                return False
        
        return True
    
    def make_move(self, marker, c):
        if marker not in [P1, P2]:
            raise ValueError('Only P1({}) and P2({}) are allowed'.format(P1, P2))

        for r in range(self.side):
            if self.grid[r][c] == EMPTY:
                self.grid[r][c] = marker
                return
        
        raise ColumnFullException()
    
    def make_copy(self):
        copy = Board(self.side)
        for r in range(self.side):
            for c in range(self.side):
                copy.grid[r][c] = self.grid[r][c]
        
        return copy
    
    def __str__(self):
        s = ''
        for r in range(self.side):
            for c in range(self.side):
                s += '|{}'.format(' ' if self.grid[r][c] == EMPTY else self.grid[r][c])
            
            s += '|\n'
        
        return s