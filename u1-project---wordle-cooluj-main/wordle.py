from enum import Enum
from typing import List, Dict
#I added import random because it is used to pick a random word form the list of stored words in WordList Object
import random

# DO NOT MODIFY THESE ENUMS/CONSTANTS; use them as is in your code
class GuessState(Enum):
   UNKNOWN = 0
   INVALID_WORD = 1
   GUESS_AGAIN = 2
   YOU_LOST = 3
   YOU_WON = 4
 
class LetterState(Enum):
   MATCH_LETTER = 0
   MATCH_PLACE = 1
   NOT_FOUND = 2
 
class TextColor:
   GREEN =  '\033[32m'
   YELLOW =  '\033[33m'
   BLACK =  '\033[30m'
   RESET =  '\033[m'

class GuessResult:
    #intitalizes user_guess and turns_remaining and has three attributes
    def __init__(self, user_guess: str, turns_remaining: int)-> None:
        self.user_guess:str = user_guess
        self.turns_remaining:int = turns_remaining
        self.state:GuessState = GuessState.UNKNOWN
        self.letter_state:LetterState = []
        self.current_word:str = ""
    #returns a string on the state of the game with the number of turns left, 
    #if the the game has been won or needs to try again
    def get_state_string (self)-> str:
        if self.state == GuessState.GUESS_AGAIN:
            return (f"{self.turns_remaining} turns left")
        elif self.state == GuessState.YOU_WON:
            return ("You Won!!")
        elif self.state == GuessState.YOU_LOST:
           return ("You lost.  Word was " + self.current_word)
        else:
           return ("Not a word, try again.")
    #get_guess_string method outputs a string of the guess by color coding the letters 
    #if the letter is a match but not in the write place it is yellow
    #if the letter is a match and is in the correct stop it is green
    #if the letter does not match any letters in the word then it is black
    #if it is not found it will be white
    #finally if will go to orginal color after is reset
    def get_guess_string(self) -> str:
        ret_str = ""
        if (self.state != GuessState.INVALID_WORD):
            for i in range (len(self.user_guess)):
                if self.letter_state[i] == LetterState.MATCH_LETTER:
                    ret_str += TextColor.YELLOW + self.user_guess[i]
                elif self.letter_state[i] == LetterState.MATCH_PLACE:
                    ret_str += TextColor.GREEN + self.user_guess[i]
                elif self.letter_state[i] == LetterState.NOT_FOUND:
                    ret_str += TextColor.RESET + self.user_guess[i]
                else:
                    ret_str += TextColor.BLACK + self.user_guess[i]
                ret_str += TextColor.RESET
        return (ret_str)

#will store and access the list of words
#methods set the active words, check if the word is vaild, and picks a random word from the list of active words
class WordList:
   #reads a file word.txt and stores each line as an element in _words and intialzies vairables _word_length and _active_words
   def __init__(self) -> None:
    with open("words.txt", "r", encoding="utf-8") as file:
        self._words = [line.rstrip() for line in file]  
    self._word_length:int = 0
    self._active_words:List[str] = []
   #set the length of the word to create a list of words with the specified length from the list of words in the text file and resets the list of active words
   def set_active_word_length (self, word_length:int)-> None:
    self._word_length = word_length
    self._active_words = []
    for x in self._words:
        if len(x) == word_length:
            self._active_words.append(x)
   #This method checks to see if a given word is valid in the list of active words if the length of the input word is the same as the length of the words in the _active_words list if the lengths are not the same it will return false.
   #After it iterates or loops through the list of active words with the use of a for loop and checks to see if any of them are the same as the given word. 
   #If it finds a match, it will return True otherwise it will return False.
   def is_valid_word(self, word:str)->bool:
    if len(word) == self._word_length:
        for x in self._active_words:
            if x == word:
                return True
    return False
   #chooses random word from a list of active words
   def pick_random_word(self)->str:
    return (random.choice(self._active_words))
# is a constant that will store the max guesses in the game
MAX_GUESSES = 5


#WordleGame class allows the user to guess a word chosen from the WordList class,with a certain number of turns. 
class WordleGame:
    #intializes new instances of the WordleGame Class
    def __init__(self) -> None:
       self.guess_left:int = MAX_GUESSES
       self.ramdom_word:str = ""
       self.has_won:bool = False
       self.is_valid_guess:bool = True
       self.is_valid_ramdom_word:bool = True
       self.word_list:WordList = []
    # this method returns a boolean value if the user has more guess left
    # if guess left is greater than zero than it will return true otherwise it will return false
    def has_more_guesses(self)->bool:
        if self.guess_left > 0:
            return True
        else:
            return False
    #intialzes a new game and creates a new word list object and sets an active word length parameter 
    #sets an _vaild_guess attribute to the result of checking whether the given test_word is a valid word of the specified length. 
    #If test_word is not an empty string, the ramdom_word attribute is set to test_word if it is a valid word or is_valid_random_word it is set to False if it is not. 
    #If test_word is an empty string, a random word of the specified length is chosen from the list of active words and assigned to the ramdom_word attribute.
    def start_new_game(self, length:int, test_word="")->None:
        self.word_list = WordList()
        self.word_list.set_active_word_length (length)
        self.is_valid_guess = self.word_list.is_valid_word(test_word)
        
        if test_word !="":
            if self.word_list.is_valid_word(test_word) is True:
                self.ramdom_word = test_word
            else:
                self.is_valid_ramdom_word = False
        else: 
            self.ramdom_word = self.word_list.pick_random_word()
    #This method is used to check the guess matches the random word and if it does it game state will turn to You Won and if it does not it will say try again or you lost.
    #It takes the guess as a string and returns it as a GuessResult object. 
    #It decrements the number of guesses left and initializes a GuessResult object with the current guess and number of turns remaining. 
    #After it sets the is_valid_guess to True if the guess is a valid word otherwise it will output False. 
    #After it checks the guess with the random word, updating the letter_state for each letter in the guess as a MATCH_PLACE, MATCH_LETTER, or NOT_FOUND. 
    #If the guess is the same as the random word, it will set the state of the GuessResult object to YOU_WON and will set has_won to True. 
    #If the number of turns remaining is 0, it will set the state to YOU_LOST and set the current_word of the GuessResult object to the random word. 
    #Otherwise, it will set the state to GUESS_AGAIN. 
    #If the guess is not a valid word, it sets the state to INVALID_WORD.         
    def submit_guess_and_get_result(self, guess:str)->GuessResult:
       self.guess_left = self.guess_left-1
       guess_result = GuessResult(guess, self.guess_left)
       self.is_valid_guess = self.word_list.is_valid_word(guess)
       if self.is_valid_guess is True:
        for i, letter in enumerate(guess_result.user_guess):
            if letter == self.ramdom_word[i]:
                guess_result.letter_state.append (LetterState.MATCH_PLACE)
            elif letter in self.ramdom_word:
                guess_result.letter_state.append(LetterState.MATCH_LETTER)
            else:
                guess_result.letter_state.append(LetterState.NOT_FOUND)
        if guess_result.user_guess == self.ramdom_word:
            guess_result.state = GuessState.YOU_WON
            self.has_won = True
        elif self.guess_left == 0:
            guess_result.state = GuessState.YOU_LOST
            guess_result.current_word = self.ramdom_word
        else:
            guess_result.state = GuessState.GUESS_AGAIN
       else:
            guess_result.state = GuessState.INVALID_WORD
       return (guess_result) 
       