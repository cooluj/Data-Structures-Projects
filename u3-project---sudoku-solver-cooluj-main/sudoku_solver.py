#imports various libraries, including 'deepcopy' from 'copy', and several typing and data structure libraries.
#'TypeVar' and 'Generic' are used for creating custom data types, 'Deque', 'Dict', 'List', 'Set', and 'Tuple' are for creating collections of data, and 'Stack' and 'Queue' are for implementing stack and queue data structures.
from copy import deepcopy
from datetime import datetime
from typing import List

# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and 
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.
#
# Your job is to write a solver that takes a sudoku puzzle and fills in all the characters correctly.
# Puzzles for this assignment use any characters, not just traditional numbers 1-9, and the
# size can vary/is not always 9x9 (side length will always be a square number). Spots that are not
# filled in have None in them.
#
# Tips:
# - Sets are your friend!
# - solve is a wrapper; you will need a recursive version of the solve function
# - It is worthwhile to consider what you should initialize before starting your recursive algorithm
# - If you are not sure where to start, use previous backtracking exercises for inspiration
# 
# Extensions: 
# 1) If you are backtracking in empty cell order, try optimizing the solver by finding more optimal empty 
#    cells to use for your subsequent recursive calls. See how fast you can get the 16x16 test to finish!:)
#    Uncomment the 16x16 advanced test to put things to the test (see if you can get it to run in under 10 min)
# 2) Use tkinter to put a UI around the solver, where you can type in your own puzzles to solve!
# 3) Write a Sudoku puzzle creator



#the purpose of this SudokuSolver class is to make a sudoku puzzle.
#it does this by creating a method called solve which takes a grid of a 2D list of strings that represents the Sudoku puzzle and solves it by filling in the empty cells with the correct values in each grid. 
#The solve method uses a recursive function called solve_recursive to try different values for each empty cell and checks to see if they are valid according to the Sudoku to the rules that each row, column and subgrid must all have unique values from 1-9. 
#If a value is valid the function will move to the next empty cell and repeats the process. 
#If no valid value are found in the cell, the function backtracks to the previous cell and tries a different value. 
#If the function is able to fill in all the empty cells without violating any rules, it returns True and the solved grid is returned by the solve method. 
#If the function is unable to find a solution, it returns False.
class SudokuSolver:

    #will intialize the sudcku solver object the given cell options and calculates the side length and the subgrids side length
    def __init__(self, cell_options:List[str]) -> None:
        self.cell_options = cell_options
        self.side_length = len(cell_options)
        self.subgrid_side_length = int(self.side_length ** 0.5)

        
    #this will create a helper function that checks if the given value is vaild to place at the postion in the grid if it is it will return true if the value is vaild and false otherise
    def is_valid(self, x, y, val, grid):
        #checks if the value is in already in the same row
        if val in grid[x]:
            return False
        #checks if the value is already in the same column
        for i in range(self.side_length):
            if grid[i][y] == val:
                return False
        #then we will check if the value is already in the same subgrid
        start_x = x - x % self.subgrid_side_length
        start_y = y - y % self.subgrid_side_length
        for i in range(self.subgrid_side_length):
            for j in range(self.subgrid_side_length):
                if grid[start_x + i][start_y + j] == val:
                    return False
        return True
   
    
    #the purpose of the of this function find_next_empty is to but the next empty portion of the grid by iterating through the rows and columns of the grid at the specfic x and y position 
    #and returning the coorderinates of he x and y postions of the empty cell and if there is no empty cell it will return none.
    def find_next_empty(self,grid, x, y):
        for i in range(x, self.side_length):
            for j in range(self.side_length):
                if grid[i][j] is None:
                    return i, j
        return None    
    
    def solve(self, grid:List[List[str]]) -> List[List[str]]:
        if(self.solve_recursive(grid, 0, 0)):
            return grid
            

    #what i wrote above the class
    #this recursive function solve_recursive tries the different values in each of the empty cells and sees if they are valid.
    #if the value is valid at the specfic function it will move to the next empty cell and will continue the process.
    #if there is no vaild value in the current cell the function will backtrack to a pervious cell with a different value
    #if that function is finally able to fill that the empty cell without breaking any of the rules in the process it will return true otherwise it will return false
    def solve_recursive(self, grid, x, y):
        #finds the next empty cell
        next_empty = self.find_next_empty(grid, x, y)
        #if there are no more empty cells, we have found a solution
        if not next_empty:
            return True
        x, y = next_empty
        #tries each possible value for the curent cell
        for val in self.cell_options:
            if self.is_valid(x, y, val, grid):
                grid[x][y] = val
                #if the current value does not match the solution it will reset the cell empty
                if self.solve_recursive(grid, x, y):
                    return True
                grid[x][y] = None

        return False
        
        



 