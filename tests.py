import unittest
from Maze import Maze

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_cell_wall_state(self):
        m1 = Maze(0, 0, 3, 3, 10, 10)
        for i, row in enumerate(m1._cells):
            for j, cell in enumerate(row):
                self.assertEqual(cell.has_left_wall, True)
                self.assertEqual(cell.has_right_wall, True)
                self.assertEqual(cell.has_top_wall, True)
                self.assertEqual(cell.has_bottom_wall, True)


    if __name__ == "__main__":
        unittest.main()