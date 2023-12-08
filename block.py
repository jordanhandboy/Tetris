class Block:
    def __init__(self, shape: list, color: tuple):
        self.shape = shape
        self.color = color
        self.pos = [4, 0]

    def get_pos(self) -> list:
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    def get_shape(self) -> list:
        return self.shape
    
    def get_color(self) -> tuple:
        return self.color
    
    def set_color(self, color):
        self.color = color

    def rotate_right(self):
        newShape = []
        for c in range(len(self.shape[0])):
            line = []
            for r in range(len(self.shape)):
                line.insert(0, self.shape[r][c])
            newShape.append(line)
        self.shape = newShape
        return self.shape
    
    def rotate_left(self):
        newShape = []
        for c in range(len(self.shape[0])):
            line = []
            for r in range(len(self.shape)):
                line.append(self.shape[r][c])
            newShape.insert(0, line)
        self.shape = newShape
        return self.shape
    
    def move_down(self):
        self.pos[1] += 1

    def move_left(self):
        self.pos[0] -= 1

    def move_right(self):
        self.pos[0] += 1

    def move_up(self):
        self.pos[1] -= 1

class BlockCreator:
    SHAPES = [[[1, 1, 1, 1]],
              
              [[1, 0, 0],
               [1, 1, 1]],

              [[0, 0, 1],
               [1, 1, 1]],
               
              [[1, 1],
               [1, 1]],
               
              [[0, 1, 1],
               [1, 1, 0]],
               
              [[1, 1, 0],
               [0, 1, 1]],
               
              [[0, 1, 0],
               [1, 1, 1]]]
    
    COLORS = [(1, 237, 250),
              (46, 46, 132),
              (255, 200, 46),
              (254, 251, 52),
              (83, 218, 63),
              (253, 63, 89),
              (221, 10, 178)]
    
    def create_block(block_id):
        return Block(BlockCreator.SHAPES[block_id], BlockCreator.COLORS[block_id])
    
# class OBlock(Block):

#     def __init__(self):
#         self.shape = [[1, 1],
#                       [1, 1]]
#         self.pos = [4, 0]
    
# class IBlock(Block):

#     def __init__(self):
#         self.shape = [[1, 1, 1, 1]]
#         self.pos = [4, 0]

# class LBlock(Block):

#     def __init__(self):
#         self.shape = [[0, 0, 1],
#                       [1, 1, 1]]
#         self.pos = [4, 0]
        
# class JBlock(Block):

#     def __init__(self):
#         self.shape = [[1, 0, 0],
#                       [1, 1, 1]]
#         self.pos = [4, 0]
        
# class SBlock(Block):

#     def __init__(self):
#         self.shape = [[0, 1, 1],
#                       [1, 1, 0]]
#         self.pos = [4, 0]

# class TBlock(Block):

#     def __init__(self):
#         self.shape = [[0, 1, 0],
#                       [1, 1, 1]]
#         self.pos = [4, 0]

# class ZBlock(Block):

#     def __init__(self):
#         self.shape = [[1, 1, 0],
#                       [0, 1, 1]]
#         self.pos = [4, 0]
