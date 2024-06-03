import csv
import random
from typing import Dict, List, Tuple
from domino import Domino
from linked_list import ChickenFootLine, LineNode
from random import randrange


# Do not modify; this is used by the tests
#peyton Helped me code

class PossibleMove:
    def __init__(self, target_line: ChickenFootLine, target_line_name:str, domino:Domino) -> None:
        self.target_line = target_line #represents where the domino can be placed
        self.target_line_name = target_line_name # name of the line where the domino can be placed
        self.domino = domino # Domino object represents the domino to be placed


#had my father sit down with me and help me with this code

class ChickenFoot:

    def __init__(self, num_of_players: int, max_pips: int) -> None:
        self.num_of_players = num_of_players #number of players in the game
        self.max_pip = max_pips # max number of pip on the domino
        

    #This is the start of the start_game method definition.
    #It takes in two parameters, an integer starting_pips and an optional list of lists of Domino 
    #objects dominos_dealt, and returns None.
    def start_game(self, starting_pips:int, dominos_dealt: List[List[Domino]] = None) -> None:

        #This creates a new Domino object with pips on both sides equal to starting_pips 
        #and assigns it to a variable starting_domino.
        starting_domino:Domino = Domino(starting_pips,starting_pips)

        #This creates a new LineNode object with starting_domino as its data and assigns it to a variable starting_node.
        starting_node = LineNode(starting_domino)

        #This sets the attribute current_foot of the ChickenFoot instance to starting_domino,
        #which is the first domino played in the game.
        self.current_foot:Domino = starting_domino

        #This sets the attribute dominos_left of the ChickenFoot instance to 6, 
        #indicating that there are 6 dominos left to be played before the round is over. 
        self.dominos_left:int = 6 

        #This sets the attribute hands of the ChickenFoot instance to dominos_dealt, 
        #which is a list of lists of Domino objects representing the hands of each player. 
        #If dominos_dealt is None, this attribute will be None.
        self.hands:List[List[Domino]] = dominos_dealt

        #This sets the attribute current_player of the ChickenFoot instance to 0, indicating that the first player will start the game.
        self.current_player:int = 0

        #This creates an empty list chicken_lines to hold the ChickenFootLine objects representing the lines of play in the game.
        self.chicken_lines:List[ChickenFootLine] = []

        #This creates 6 ChickenFootLine objects using starting_node as the first node in each line, 
        #and adds them to chicken_lines. 
        #This creates the 6 lines of play in the game.
        for i in range(6):
            self.chicken_lines.append(ChickenFootLine(starting_node))


    #This method takes no arguments and returns a list of PossibleMove objects.
    def find_moves(self) -> List[PossibleMove]: 
        #Creates an empty list to store possible moves.
        possible_moves:List[PossibleMove] = []
        #Get the current player's hand of dominos.
        player_hand:List[Domino] = self.hands[self.current_player]
        #Loops through each domino in the player's hand, and for each domino, 
        for domino in player_hand:
            #loop through each chicken foot line on the board.
            for line in self.chicken_lines:
                #If the current foot is not None and the first domino in the current chicken foot line is the same as the current foot, 
                #and the current domino can be placed on the current foot, 
                #then create a PossibleMove object and append it to the possible_moves list.
                #If the current foot is None and the current domino can be placed on the open value of the first domino in the current chicken foot line, 
                #then create a PossibleMove object and append it to the possible_moves list.
                if (self.current_foot != None and domino.contains_val(self.current_foot.value[0]) and line.first.domino == self.current_foot) \
                    or (self.current_foot == None and domino.contains_val(line.first.domino.open_value)):
                    #Create a PossibleMove object that has the current chicken foot line, 
                    #the name of the line, 
                    #and the current domino.
                    possible_moves.append(PossibleMove(line,line.line_name,domino))


        #Returnsthe list of possible moves.
        return possible_moves   
    #This method adds a domino to the current player's hand. 
    #If no domino is provided, it adds a random domino from the remaining dominoes.
    def draw_domino(self, domino:Domino = None) -> Domino:
    
        #Assigns the current player's hand to a variable called hand.
        hand:List[Domino] = self.hands[self.current_player]
        #Adds the domino argument to the end of the hand list.
        hand.append(domino)
    

    def place_domino(self, domino:Domino, place) -> None:
        # Check if a double domino was played and update the game state accordingly
        if self.current_foot != None:
            self.dominos_left -= 1
            
            if self.dominos_left == 0:
                self.current_foot = None
    
        # Set the open value of the played domino to the open value of the line it was played on
        domino.set_open_value(place.first.domino.open_value)
        # Add the played domino to the line it was played on
        place.add(domino)
 

        # If a double domino was played, create new lines and add them to the game state
        if domino.is_double():
            self.current_foot = domino
            new_node = LineNode(domino)
            self.dominos_left = 3
            new_line = ChickenFootLine(new_node)
            new_line.line_name = place.line_name
            self.chicken_lines.append(new_line)
            new_line = ChickenFootLine(new_node)  
            new_line.line_name = place.line_name    
            self.chicken_lines.append(new_line)
            
 
    # This method ends the turn of the current player and switches to the next player in the list.
    # If the current player is the last player in the list, then the first player in the list becomes the next player.

    def end_turn(self) -> None:
        if self.current_player < self.num_of_players-1:
            self.current_player += 1
        else:
            self.current_player = 0


    #This method returns a list of strings representing the names of all the lines on the game board.
    def get_board_paths(self) -> List[str]:
        paths:List[str] = []
        for i in range (len(self.chicken_lines)):
            paths.append(self.chicken_lines[i].line_name)
        return paths

