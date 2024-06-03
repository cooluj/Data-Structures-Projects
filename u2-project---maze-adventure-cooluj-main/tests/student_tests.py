from unittest import TestCase
from maze_adventure import MazeRoom, ROOM_KEY, TIME_NEEDED_KEY, Maze, TIME_TAKEN_TO_ARRIVE_HERE_KEY

class maze_adventure_student_tests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_student_case_invalid_room(self):
       map = {
          "A" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}]),
          "B" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}])
      }
       maze = Maze(map, "C", "D")
       solution = maze.solve_maze()
       self.assertIsNone(solution)