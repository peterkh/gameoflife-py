"""
Module contains the Grid class that represents a single game tick state.
"""

def make_grid_row(length):
    """Create a row of length with each element set to value."""
    row = []
    for _ in range(0, length):
        row.append(False)
    return row

class Grid:
    """
    Grid class, contains the state of the game in a single tick.
    """
    def __init__(self, x, y):
        self.rows = x
        self.cols = y
        self.last_row = x - 1
        self.last_col = y - 1
        self.grid = []
        for _ in range(0, self.rows):
            self.grid.append(make_grid_row(self.cols))
        self.neighbor_lookup = []

    def get_coord(self, x, y):
        """ Return the value of cell x, y in grid """
        return self.grid[x][y]

    def set_coord(self, x, y, value):
        """ Set the value of cell x, y in gird """
        self.grid[x][y] = value

    def get_neighbours(self, x, y):
        """ Return a set of tuples of all valid neighbours."""
        neighbours = set()
        if x > 0:
            if y > 0:
                neighbours.add((x - 1, y - 1))
            neighbours.add((x - 1, y))
            if y < self.last_col:
                neighbours.add((x -1, y + 1))
        if y > 0:
            neighbours.add((x, y - 1))
            if x < self.last_row:
                neighbours.add((x + 1, y - 1))
        if x < self.last_row:
            neighbours.add((x + 1, y))
            if y < self.last_col:
                neighbours.add((x + 1, y + 1))
        if y < self.last_col:
            neighbours.add((x, y + 1))
        return neighbours

    def populate_neighbours(self):
        """ Create a neighbor lookup grid """
        self.neighbor_lookup = []
        for row in range(0, self.rows):
            row_list = []
            for col in range(0, self.cols):
                row_list.append(self.get_neighbours(row, col))
            self.neighbor_lookup.append(row_list)

    def alive_neighbours(self, x, y):
        """ Number of alive neighbours cell x, y has """
        neighbors = self.neighbor_lookup[x][y]
        total_alive = 0
        for neighbor in neighbors:
            if self.get_coord(neighbor[0], neighbor[1]):
                total_alive += 1
        return total_alive
