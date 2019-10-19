# NISHANT MAHAJAN
# 2017A7PS0112P

from board import P1, P2, Board, ColumnFullException
from game import Game
from robot import Robot
from state import State
from tkinter import ttk, messagebox
from tkinter import *

class Gui:
    def __init__(self, width = 480, height = 480):
        self.game = None

        self._layout_root = Tk()
        self._layout_root.title('Assignment #3')
        self._layout_root.geometry("{}x{}".format(width, height))
        self._layout_root.rowconfigure(0, weight=1)
        self._layout_root.columnconfigure(0, weight=1)

        main_frame = ttk.Frame(self._layout_root, padding='10 10 10 10')
        main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

        ttk.Button(main_frame, text='New Game', command=self._on_new_game).grid(row=0, column=0, padx=(10, 20))
        ttk.Button(main_frame, text='See Data', command=self._on_see_data).grid(row=1, column=0, padx=(10, 20))

        self._canvas = Canvas(main_frame)
        self._canvas.grid(row=0, column=1, rowspan=4, columnspan=4)
        self._canvas.bind('<Button-1>', self._mouse_click)

        self.bs_offset = 40
    
    def loop(self):
        self._layout_root.mainloop()
    
    def _on_new_game(self):
        self.game = Game()
        
        self._paint_board()
        self.game.advance()
        self._paint_board()
    
    def _on_see_data(self):
        messagebox.showinfo('Coming soon', 'This section is a WIP')
    
    def _mouse_click(self, event):
        if self.game is None:
            messagebox.showwarning('Wait', 'No game is active. Please start a new one')
            return

        if self.game.p1_turn() or self.game.is_over():
            return
        
        try:
            self.game.make_human_move(int(event.x / self._square_size()) % 4)
        except ColumnFullException:
            messagebox.showwarning('Illegal Move', 'Illegal Move. The column is already full. The game is forfeited. Start a new game')
            return

        self._paint_board()

        if self.game.is_over():
            self._show_ending()
            self.game = None
            return

        self.game.advance()
        self._paint_board()

        if self.game.is_over():
            self._show_ending()
            self.game = None
            return
    
    def _paint_board(self):
        self._canvas.delete('all')

        size = self._square_size()

        self._canvas.create_rectangle(1, 15, size * 4 + 1, 25, fill='red')

        for r in range(self.game.state.board.side):
            for c in range(self.game.state.board.side):
                x = c * size + 1
                y = r * size + 1 + self.bs_offset 
                self._canvas.create_rectangle(x, y, x + size, y + size, outline='black')
                if self.game.state.board.grid[r][c] == P1:
                    self._canvas.create_oval(x, y, x + size, y + size, fill='green')
                if self.game.state.board.grid[r][c] == P2:
                    self._canvas.create_oval(x, y, x + size, y + size, fill='blue')


    def _show_ending(self):
        winner = self.game.state.board.check_winner()

        result = 'Match ended in a draw'

        if winner == P1:
            result = 'P1 won the game'
        if winner == P2:
            result = 'P2 won the game'

        messagebox.showinfo('Game Over', result)

    def _square_size(self):
        dim = min(self._canvas.winfo_width(), self._canvas.winfo_height() - self.bs_offset)
        return (dim / self.game.state.board.side) - 1
