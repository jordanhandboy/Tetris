from block import *
from copy import deepcopy

class TetrisGame():
    def __init__(self, rows=20, columns=10):
        self.rows = rows
        self.columns = columns
        self.board = [[0] * columns for i in range(rows)]
        self.current_block = 0
        self.views = []

    def add_block(self, block, x=4, y=0):
        self.current_block = block
        self.update()

    def add_view(self, view):
        self.views.append(view)

    def notify_views(self):
        for view in self.views:
            view.draw_board()

    def place_block(self):
        self.current_block = 0

    def update(self, prev_pos=False, prev_shape=False):
        if prev_pos or prev_shape:
            for i in range(len(prev_shape)):
                for j in range(len(prev_shape[0])):
                    self.board[i+prev_pos[1]][j+prev_pos[0]] -= prev_shape[i][j]
        shape = self.current_block.get_shape()
        pos = self.current_block.get_pos()
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                self.board[i+pos[1]][j+pos[0]] += shape[i][j]
        self.notify_views()

    def rotate_right(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.rotate_right()
        self.update(prev_pos, prev_shape)

    def rotate_left(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.rotate_left()
        self.update(prev_pos, prev_shape)

    def move_down(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_down()
        self.update(prev_pos, prev_shape)

    def move_left(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_left()
        self.update(prev_pos, prev_shape)

    def move_right(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_right()
        self.update(prev_pos, prev_shape)

    def get_board(self):
        return self.board

    def __str__(self):
        output = ""
        for line in self.board:
            for cell in line:
                if cell == 1:
                    output += "X"
                elif cell == 0:
                    output += "."
                else:
                    output += "?"
            output += "\n"
        return output

    