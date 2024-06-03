from collections import deque

class LinkedListNode:
    def __init__(self, value) -> None:
        pass

class LinkedList:
    def __init__(self) -> None:
        pass

    # insert value at index position in the list and return the new node
    # raise IndexError if it is not a valid index (code ex: raise IndexError())
    def insert(self, index:int, value)->LinkedListNode:
        pass

    # remove and return the item at index
    # raise IndexError if it is not a valid index
    def pop(self, index:int) -> LinkedListNode:
        pass

    # append value to the end of the list and return the new node
    def append(self, value) -> LinkedListNode:
        pass

    # returns the number of items in the list
    # used so len() can tell you how many items are in the list
    def __len__(self)->int:
        pass

    # set a value at index
    def set(self, index:int, value) -> None:
        pass

    # returns the index of the first appearance of value
    # raise IndexError if it is not a valid index
    def find_index(self, value) -> int:
        pass

    # empties the list
    def clear(self) -> None:
        pass
