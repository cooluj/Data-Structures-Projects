from unittest import TestCase
from chicken_foot import ChickenFoot
from chicken_foot_tests import ChickenFootTests
from domino import Domino

class chicken_foot_student_tests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_student_case(self):
        game = ChickenFoot(2, 5)
        game.start_game(3, [
            [Domino(3, 5), Domino(1, 2), Domino(3, 4)],
            [Domino(1, 3), Domino(2, 5), Domino(2, 4)]
        ]
        )
        moves = game.find_moves()
        self.assertEqual(12, len(moves))


    