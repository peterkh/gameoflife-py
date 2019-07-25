from .context import gameoflife

import unittest

class GridTestSuite(unittest.TestCase):
    """Grid class test cases."""

    def test_grid_init(self):
        grid = gameoflife.Grid(4, 5)
        assert(grid.last_row == 3)
        assert(grid.last_col == 4)
        assert(len(grid.grid) == 4)
        assert(len(grid.grid[0]) == 5)

    def test_make_grid_row(self):
        assert(gameoflife.grid.make_grid_row(4) == [False, False, False, False])

    def test_get_coord(self):
        grid = gameoflife.Grid(4, 5)
        assert(grid.get_coord(3, 4) == False)

    def test_set_coord(self):
        grid = gameoflife.Grid(6,3)
        grid.set_coord(5, 2, True)
        assert(grid.get_coord(5, 2) == True)

    def test_get_neighbours(self):
        grid = gameoflife.Grid(4,5)
        # middle, full set of neighbours
        neighbours = grid.get_neighbours(2,2)
        assert(neighbours == {
            (1,1), (1,2), (1,3), (2,1), (2,3), (3,1), (3,2), (3,3)
            })
        # top corner
        neighbours = grid.get_neighbours(0,0)
        assert(neighbours == {
            (1,1), (1,0), (0,1)
            })
        #bottom corner
        neighbours = grid.get_neighbours(3,4)
        assert(neighbours == {
            (2,3), (3,3), (2,4)
            })
        # bottom row
        neighbours = grid.get_neighbours(2,4)
        assert(neighbours == {
            (1,3), (1,4), (2,3), (3,3), (3,4)
            })

    def test_populate_neighbours(self):
        grid = gameoflife.Grid(4,5)
        grid.populate_neighbours()
        assert(grid.neighbor_lookup[2][1] == grid.get_neighbours(2, 1))
        assert(grid.neighbor_lookup[3][4] == grid.get_neighbours(3, 4))

    def test_alive_neighbours(self):
        grid = gameoflife.Grid(10,12)
        grid.populate_neighbours()
        assert(grid.alive_neighbours(3,3) == 0)
        grid.set_coord(2,3, True)
        grid.set_coord(3,4, True)
        assert(grid.alive_neighbours(3,3) == 2)
              

if __name__ == '__main__':
    unittest.main()
