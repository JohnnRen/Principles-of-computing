"""
Clone of 2048 game.
"""

import random
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Collapse empty grid
    line_org = tuple(line)
    for _ in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for index in range(1, len(line)):
        if line[index] == 0:
            break
        if line[index] == line[index - 1]:
            line[index - 1] *= 2
            del line[index]
            line.append(0)
    return tuple(line) != line_org


class Grid(object):
    """Implementation of grid object"""
    _data = []
    _grid_height = 0
    _grid_width = 0

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def get(self, row=0, col=0):
        """Get the value at the given position"""
        return self._data[row][col]

    def set(self, row, col, value):
        """Set the value at the given position"""
        self._data[row][col] = value

    def get_data(self):
        """Get the data as a list"""
        return self._data

    def reset(self):
        """Reset the grid"""
        self._data = [[0 for _ in range(self._grid_width)]
                      for _ in range(self._grid_height)]

    def get_pos_generator(self, start, offset):
        """Get a generator which iterate the position"""
        current = start
        index = 1
        yield current[0], current[1], index
        while True:
            current = [current[0] + offset[0], current[1] + offset[1]]
            if self._grid_height - 1 >= current[0] >= 0 and self._grid_width - 1 >= current[1] >= 0:
                index += 1
                yield current[0], current[1], index
            else:
                break

    def get_line(self, line_index, direction):
        """Get a line of the grid"""
        line = []
        offset = OFFSETS[direction]
        start = {UP: [0, line_index],
                 DOWN: [self._grid_height - 1, line_index],
                 LEFT: [line_index, 0],
                 RIGHT: [line_index, self._grid_width - 1]
                 }[direction]
        for row, col, _ in self.get_pos_generator(start, offset):
            line.append(self.get(row, col))
        return line

    def set_line(self, line_index, direction, line):
        """Set a line of the grid by providing a list"""
        offset = OFFSETS[direction]
        start = {UP: [0, line_index],
                 DOWN: [self._grid_height - 1, line_index],
                 LEFT: [line_index, 0],
                 RIGHT: [line_index, self._grid_width - 1]
                 }[direction]
        for row, col, index in self.get_pos_generator(start, offset):
            self.set(row, col, line[index - 1])


class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """
    grid = None
    grid_width = 4
    grid_height = 4

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = Grid(self.grid_height, self.grid_width)
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid.get_data())

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        has_moved = False
        offset = OFFSETS[direction]
        line_index_iterator = range(
            self.grid_width if offset[1] == 0 else self.grid_height)
        for index in line_index_iterator:
            line = self.grid.get_line(index, direction)
            has_moved = merge(line) or has_moved
            self.grid.set_line(index, direction, line)
        if has_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        value = 2 if random.random() < 0.9 else 4
        row = random.choice(range(self.grid_height))
        col = random.choice(range(self.grid_width))
        if self.get_tile(row, col) == 0:
            self.set_tile(row, col, value)
        else:
            self.new_tile()

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid.set(row, col, value)

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid.get(row, col)


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
