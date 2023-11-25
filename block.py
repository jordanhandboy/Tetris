class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.pos = [4, 0]

    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos

    def get_shape(self):
        return self.shape

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
    
    def create_block(block_id):
        return Block(BlockCreator.SHAPES[block_id], block_id)
    
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
