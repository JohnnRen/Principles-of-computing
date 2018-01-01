UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


class Grid(object):
    _data = []
    _grid_height = 0
    _grid_width = 0

    def __init__(self, grid_height, grid_width):
        self._data = [[0 for _ in range(grid_width)]
                      for _ in range(grid_height)]
        self._grid_height = grid_height
        self._grid_width = grid_width

    def get(self, y=0, x=0):
        return self._data[y][x]

    def set(self, y, x, value):
        self._data[y][x] = value

    def get_data(self):
        return self._data

    def reset(self):
        self.__init__(self._grid_height, self._grid_width)

    def get_pos_generator(self, start, offset):
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
        offset = OFFSETS[direction]
        start = {UP: [0, line_index],
                 DOWN: [self._grid_height - 1, line_index],
                 LEFT: [line_index, 0],
                 RIGHT: [line_index, self._grid_width - 1]
                 }[direction]
        for row, col, index in self.get_pos_generator(start, offset):
            self.set(row, col, line[index - 1])
