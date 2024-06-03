from typing import List
import unittest
from wordle import WordList, GuessResult, GuessState, LetterState, WordleGame

"""
Instructions:
Write a test case for any function that you implemented
"""
class StudentTestCases(unittest.TestCase):
    """
    def test_student_case(self):
        pass
    """
    def setUp(self) -> None:
        self.game: WordleGame = WordleGame()
        return super().setUp()

    def _assert_game_result(self, 
                            result: GuessResult, 
                            guess: str, 
                            letter_states: List[LetterState],
                            guesses_left: int, 
                            state: GuessState) -> None:

        result_string = result.get_state_string()

        if state == GuessState.YOU_WON:
            self.assertEqual(result_string, "You Won!!")
            
    def test_win_after_multiple_attempts(self):
        self.game.start_new_game(6, "wolves")

        result = self.game.submit_guess_and_get_result("runner")
        result = self.game.submit_guess_and_get_result("zipped")
        result = self.game.submit_guess_and_get_result("waiter")
        result = self.game.submit_guess_and_get_result("wishes")
        result = self.game.submit_guess_and_get_result("wolves")
        self._assert_game_result(
            result, "wolves", [LetterState.MATCH_PLACE, 
            LetterState.MATCH_PLACE, LetterState.MATCH_PLACE, 
            LetterState.MATCH_PLACE, LetterState.MATCH_PLACE, LetterState.MATCH_PLACE], 0, 
            GuessState.YOU_WON)
