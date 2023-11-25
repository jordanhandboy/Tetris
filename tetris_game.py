from block import *
from copy import deepcopy
import random

class TetrisGame():
    def __init__(self, rows=20, columns=10):
        self.rows = rows
        self.columns = columns
        self.board = [[0] * columns for i in range(rows)]
        self.current_block = 0
        self.views = []

    def add_view(self, view):
        self.views.append(view)

    def notify_views(self):
        for view in self.views:
            view.draw_board()

    def add_block(self, block, x=4, y=0):
        self.current_block = block
        self.update()

    def place_block(self):
        self.current_block = 0
        self.check_lines()
        self.generate_block()

    def check_lines(self):
        for i in range(len(self.board)):
            found_zero = False
            for cell in self.board[i]:
                if cell == 0:
                    found_zero = True
            if not found_zero:
                self.clear_line(i)

    def clear_line(self, line):
        self.board.pop(line)
        self.board.insert(0, [0 for i in range(self.columns)])

    def generate_block(self):
        self.add_block(BlockCreator.create_block(random.randrange(0, 7)))

    def update(self, prev_pos=False, prev_shape=False):
        if prev_pos or prev_shape:
            for i in range(len(prev_shape)):
                for j in range(len(prev_shape[0])):
                    if self.board[i+prev_pos[1]][j+prev_pos[0]] - prev_shape[i][j] < 0:
                        raise ValueError
                    self.board[i+prev_pos[1]][j+prev_pos[0]] -= prev_shape[i][j]
        shape = self.current_block.get_shape()
        pos = self.current_block.get_pos()
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if self.board[i+pos[1]][j+pos[0]] + shape[i][j] > 1:
                    raise ValueError
                self.board[i+pos[1]][j+pos[0]] += shape[i][j]
        self.notify_views()

    def test_update(self, prev_pos=False, prev_shape=False):
        test_board = deepcopy(self.board)
        if prev_pos or prev_shape:
            for i in range(len(prev_shape)):
                for j in range(len(prev_shape[0])):
                    if self.board[i+prev_pos[1]][j+prev_pos[0]] - prev_shape[i][j] < 0:
                        raise ValueError
                    test_board[i+prev_pos[1]][j+prev_pos[0]] -= prev_shape[i][j]
        shape = self.current_block.get_shape()
        pos = self.current_block.get_pos()
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if test_board[i+pos[1]][j+pos[0]] + shape[i][j] > 1:
                    raise ValueError
                test_board[i+pos[1]][j+pos[0]] += shape[i][j]

    def rotate_right(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.rotate_right()
        try:
            self.test_update(prev_pos, prev_shape)
        except:
            self.current_block.rotate_left()
        else:
            self.update(prev_pos, prev_shape)

    def rotate_left(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.rotate_left()
        try:
            self.test_update(prev_pos, prev_shape)
        except:
            self.current_block.rotate_right()
        else:
            self.update(prev_pos, prev_shape)

    def move_down(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_down()
        try:
            self.test_update(prev_pos, prev_shape)
        except:
            self.current_block.move_up()
        else:
            self.update(prev_pos, prev_shape)

    def move_left(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_left()
        if self.current_block.get_pos()[0] < 0:
            self.current_block.move_right()
        try:
            self.test_update(prev_pos, prev_shape)
        except:
            self.current_block.move_right()
        else:
            self.update(prev_pos, prev_shape)

    def move_right(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_right()
        try:
            self.test_update(prev_pos, prev_shape)
        except:
            self.current_block.move_left()
        else:
            self.update(prev_pos, prev_shape)

    def drop(self):
        prev_pos = deepcopy(self.current_block.get_pos())
        prev_shape = deepcopy(self.current_block.get_shape())
        self.current_block.move_down()
        while True:
            try:
                self.test_update(prev_pos, prev_shape)
            except:
                self.current_block.move_up()
                break
            else:
                self.current_block.move_down()
        self.update(prev_pos, prev_shape)
        self.place_block()

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

    