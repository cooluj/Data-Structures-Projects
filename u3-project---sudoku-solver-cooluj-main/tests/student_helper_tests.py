from unittest import TestCase
from sudoku_solver import SudokuSolver

class SudokuSolverStudentTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_find_next_empty(self):
        solver = SudokuSolver(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        grid = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
        ]
        expected_output = ( 6, 0)
        self.assertEqual(expected_output, solver.find_next_empty(grid, 0, 0))
        