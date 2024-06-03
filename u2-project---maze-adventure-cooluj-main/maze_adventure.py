#imports various libraries, including 'deepcopy' from 'copy', and several typing and data structure libraries. 
#'TypeVar' and 'Generic' are used for creating custom data types, 'Deque', 'Dict', 'List', 'Set', and 'Tuple' are for creating collections of data, and 'Stack' and 'Queue' are for implementing stack and queue data structures.
from collections import deque
from copy import deepcopy
from typing import Deque, Dict, Generic, List, Set, Tuple, TypeVar
from stack_queue import Stack, Queue

T = TypeVar("T")
    
# U2 Project: Maze Adventure Solver
# **************************************************
# Welcome to the Maze Adventure, a labyrinth where you have to help the user find the path of shortest 
# duration to get from a start room to an end room. Implement the Maze class, which stores a maze in the form of a 
# dictionary of rooms with properties on them and finds a path through in the method solve_maze. This project
# also comes with an optional extension for the more adventurous where you need to obtain items to unlock some 
# of the rooms.  Look for "Locked Room Extension" in the comments to know what is optional. 
# 
# The solver will use a classic Breadth First Search algorithm (see OneNote) and put your Stack, Queue, Set, and Map skills to the 
# test, which offers you this chilling challenge: to find a way out, muahaha!  Of course, there's always my way...
# https://studio.code.org/projects/applab/1WKMHhvvCKtuTaZMJKRqLK09DhGdKLQb3jOTy3Cye7E

# Constants for keys to the dictionaries
ROOM_KEY = "room_name"
TIME_NEEDED_KEY = "time_needed"
TIME_TAKEN_TO_ARRIVE_HERE_KEY = "time_taken"


# Class: MazeRoom 
# **************************************************
# Stores the properties of a room in the labyrinth
# rooms_you_can_go_to (List[Dict]): A list of rooms you can get to from the current room. Each list item is a dictionary that
# contains the following key/value pairs:
#       Key (str): "room_name" (represented by constant ROOM_KEY) / Value (str): The name of the neighboring room
#       Key (str): "time_needed" (represented by constant TIME_NEEDED) / Value (int): time it takes to get to the neighboring room
#                   from the current room
# item (opt str used for the Locked Room extension only): the item that is contained in the room if any
# requires (opt str used for the Locked Room extensicoon only): the item required to unlock the room if any
# Note: you can add whatever attributes you would like to this class.  It does not have to be limited to the parameters
class MazeRoom:
    def __init__(self, rooms_you_can_go_to: List[Dict], item: str = None, requires: str = None) -> None:
      
       self.rooms_you_can_go_to:List[Dict] = rooms_you_can_go_to
       self.item:str = item
       self.requires:str = requires
  
 
# Class: Maze
# ***************************************************
# Stores the map and finds the shortest duration path.  Special properties of the map:
#   -The map stores information about each room, including what rooms are connected to it and how long it
#    takes to get to that room.  Rooms can be large, so it takes more time to get to some rooms (see MazeRoom
#    class description)
#   -You should not visit the same room more than once (unless you are doing the locked door extension)
#   -Some mazes are not solvable.  In this case, the returned stack should be None
class Maze:
 
   # Constructor
   # ***************************************************
   # Parameters:
   # maze: a dictionary of all the rooms in the labyrinth and their properties. Contains key/value pairs:
   #     Key: the name of the room
   #     Value: a MazeRoom object (you should feel free to modify this object as needed)
   # start_room (str): the name of the room where you start
   # end_room(str): the name of the room you need to get to
   #
   # Note: you can add whatever attributes you would like.  It does not have to be limited to the parameters.
    def __init__(self, maze: Dict, start_room: str, end_room: str) -> None:  
       self.maze:Dict = maze
       self.start_room:str = start_room
       self.end_room:str = end_room

    # solve_maze
    # ***************************************************
    # Finds the path of shortest duration to get from the start room to the end room.  
    # Returns a stack of dictionaries representing the shortest path, with the end room at the top of the stack and 
    # start room at the bottom. The dictionaries must include (but is not limited to) the following key/value pairs:
    #       Key (str): "room_name" (represented by constant ROOM_KEY) / Value (str): name of the room
    #       Key (str): "time_taken" (represented by constant TIME_TAKEN_TO_ARRIVE_HERE_KEY)) / 
    #                       Value (int): number of steps it took to get to this room
    # If there is no solution, this method returns None
    #
    # Important: Use deepcopy(object) to make separate copies of an object and all its inner components. Also
    # the start room should have 0 as its time taken.
    def solve_maze(self) -> Stack[Dict]:
        #current_room is a local varible which will store the current room.
        #this method first assigns the current_room with the start room which is given when we instintiate the maze class 
        current_room:str = self.start_room
        # this variable will track the time needed that comes from the map using the TIME_NEEDED_KEY
        time_needed:int = 0
        # this variable will track the time it took with is calculated using the TIME_TAKEN_TO_ARRIVE_HERE_KEY
        time_taken:int = 0
        #this will initiate a queue which will store the stack of different path
        queue = Queue[Stack]()
        #this will intiatie a stack which stores the a particular path. 
        stack = Stack[Dict]()
        #first we will push the start node into the stack 
        stack.push({ROOM_KEY:current_room, TIME_NEEDED_KEY:time_needed, TIME_TAKEN_TO_ARRIVE_HERE_KEY:time_taken})
        #then we will push that stack into the queue
        queue.enqueue(stack)
        #this variable stores the information about which has already been visited via a set
        room_visited = set()
        #next we will loop through the queue until we have visted all the elements of the queue
        while not queue.is_empty():
            #will remove the first element of the queue (fifo) of the type stack
            stack = queue.dequeue()
            #now we will read the top element of the stack and assign this as the current room
            current_room = stack.peek()[ROOM_KEY]
            #mark the current room as visted
            room_visited.add(current_room)
            #here the program checks if the current room is the end room meaning we already reach the final destination if so then we return the entire stack which is the shortest path 
            if current_room == self.end_room:
                #returns stack of path
                return (stack)
            # will loop through all the elements of the given map (part of the maze class input parameter)
            for key, val in self.maze.items():
                #key variable is the first room of the input map.
                #this condition will check if the first node is the current node
                if (key == current_room):
                    #if so then the program will sort the neighbors of the current room in the order of the shortest of amount of time needed. 
                    #by sorting program will have the first nieghtbor as the shortest path.
                    # for sorting dictionary object the program uses the sorted() method for this I used the lamba function and used an example i found in this article https://realpython.com/sort-python-dictionary/
                    sorted_room_based_on_time_needed = sorted (val.rooms_you_can_go_to, key=lambda x:x[TIME_NEEDED_KEY])
                    # this for loops through all the nieghhors of the given node
                    for item in sorted_room_based_on_time_needed:
                        #if the room is not already visted then push that nieghbhor in the stack
                        if item[ROOM_KEY] not in room_visited:
                            #beffore i push the nieghbor in the stack I have to make a deepcopy funciton to copy the current stack. 
                            #A current room may have more than one neighbhor in order to track the path from the current room to all the nieghbhors, 
                            # I will creat each unique path as a separate stacks which are stored into a queue.
                            #copy stack is a copy of current stack
                            copy_stack = deepcopy(stack)
                            #push the nieghbor room into the stack
                            copy_stack.push({ROOM_KEY:item[ROOM_KEY], TIME_NEEDED_KEY:item[TIME_NEEDED_KEY], TIME_TAKEN_TO_ARRIVE_HERE_KEY: item[TIME_NEEDED_KEY]})
                            #now push that stack in the queue
                            queue.enqueue(copy_stack)

        #if no end room found then return none
        return (None)


    # implements_locked_room_extension (optional for Locked Room Extension only)
    # ***************************************************
    # Make this return True if you implemented code for the Locked Room extension to enable the tests
    def implements_locked_room_extension(self) -> bool:
            return False
