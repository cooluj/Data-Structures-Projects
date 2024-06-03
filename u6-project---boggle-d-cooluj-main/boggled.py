from typing import List, Tuple, Set

#got some help from Payton and my father


class TrieNode:
    def __init__(self, letter=None) -> None:
        self.letter = letter
        # add attributes for whether it is the end of a word and a collection of pointers to
        # next letters
        self.end_of_word: bool = False      
        self.letters:dict[str,TrieNode] = {}   # here is the key value pair where the str that represents each letter is the key and trie is the value
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    def generate_tree_from_file(self,suffix:str,)->None:

        words = self._load_words()
        #add code here to set up the TrieNode tree structure for the words

        #reverse the suffix so that last letter of the word is the first letter
        suffix = suffix[::-1] 
        for word in words:
            is_valid = True
            last_node = self.root
            word = word[::-1]
            #this will make sure that len of the words is greater than the len of the suffix 
            if len(word) > len(suffix):
                for i in range(0,len(word)):
                    if i < len(suffix):#check for suffix match
                        if suffix[i] != word[i]:
                            is_valid = False #the word does not contain the suffix it is invalid and will not continue to be added
                            break
                    if not word[i] in last_node.letters.keys():
                        last_node.letters[word[i]] = TrieNode(word[i])
                    last_node = last_node.letters[word[i]]
            else:
                is_valid = False
            if is_valid:
                last_node.end_of_word = True
    # helper to load words. No modifications needed
    def _load_words(self) -> List:
        words = []
        with open("words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                words.append(word)
        return words
# Implement the Boggled Solver. This Boggle has the following special properties:
# 1) All words returned should end in a specified suffix (i.e. encode the trie in reverse)
# 2) Board tiles may have more than 1 letter (e.g. "qu" or "an")
# 3) The number of times you can use the same tile in a word is variable
# Your implementation should account for all these properties.
directions:List[Tuple] = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
class Boggled:
    # setup test initializes the game with the game board and the max number of times we can use each
    # tile per word
    def setup_board(self, max_uses_per_tile: int, board:List[List[str]])->None:
        self.board = board
        self.max_uses = max_uses_per_tile
    # Returns a set of all words on the Boggle board that end in the suffix parameter string. Words can be found
    # in all 8 directions from a position on the board
    def get_all_words(self, suffix:str)->Set:
        self.found:set[str] = set()
        self.suffix:str = suffix
        self.used_tiles:dict = {}
        trie:Trie = Trie()
        trie.generate_tree_from_file(suffix)
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.get_all_words_recursive((i,j),trie.root,"")
                self.used_tiles.clear()
        return self.found
    # recursive helper for get_all_words. Customize parameters as needed; you will likely need params for
    # at least a board position and tile
    def get_all_words_recursive(self,pos:tuple,node:TrieNode,word)->set:

        #gets the letter at the current postion of the board
        tile = self.board[pos[0]][pos[1]]

        #checks if the second letter is vaild or not by adding it to the beginning of the current words and updates the current node
        if len(tile) == 2: #handle doubles
            if tile[1] in node.letters:
                word = tile[1] + word
                node = node.letters[tile[1]]
                #updates the tile the first letter of the double leter 
                tile = tile[0]

        #this will concatenate the tile and current word
        temp = tile + word 
        #if the tile is a child of its current TrieNode and is the end of that vaild word it will add it to the set
        if tile in node.letters and node.letters[tile].letters == None and node.letters[tile].end_of_word and temp not in self.found:#base case

            self.found.add(word)
        else:
            #if the tile is a vaild child of the TireNode it will continue the recursive function and search for words
            if tile in node.letters: #base case
                word = tile + word
                if node.letters[tile].end_of_word:
                    self.found.add(word)
                next_node = node.letters[tile]
               

                #if the current postion has not been used before add it to the used_tiles dictionary with a count of 1               
                if not pos in self.used_tiles.keys(): #backtracking exclude 
                    self.used_tiles[pos] = 1
                               
                               
                # If the current position has been used before, increment its count in the used_tiles dictionary
                else:
                    self.used_tiles[pos] += 1


                # Iterate over each direction and check if the next position is on the board and can be reused
                for d in directions:
                    next_pos = self.calculate_position(pos,d)
                    if self.is_on_board(next_pos) and self.can_reuse(next_pos): #base case
                        

                        # If the next position is valid, continue searching recursively from that position
                        self.get_all_words_recursive(next_pos,next_node,word)
                            
                            
                #Decrement the count of the current position in the used_tiles dictionary and remove it if the count is 0
                self.used_tiles[pos] -= 1 #backtracking include case
                if self.used_tiles[pos] <= 0:
                  self.used_tiles.pop(pos)

    def is_on_board(self,pos:tuple) -> bool:
        return (pos[0] < len(self.board)) and (pos[1] < len(self.board)) and ( pos[0] >= 0) and ( pos[1] >= 0)
    def calculate_position(self,pos:tuple,dir:tuple):
        y = pos[0] + dir[0]
        x = pos[1] + dir[1]
        return (y,x)
   
    def can_reuse(self,pos:tuple)->bool:
        return not pos in self.used_tiles.keys() or self.used_tiles[pos] < self.max_uses
  
       