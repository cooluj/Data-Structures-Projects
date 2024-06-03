class DoubleListNode:
    def __init__(self, value) -> None:
        self.next = None
        self.previous = None
        self.value = value

class DoubleLinkedList:
    def __init__(self) -> None:
        pass

    # inserts value after node and return the new node
    # pass none for None if it is inserted in the head
    # raise ValueError if the node is not in the list
    def insert_after(self, node:DoubleListNode, value) -> DoubleListNode:
        pass

    # removes node from the list
    # raise TypeError if node is None
    # raise ValueError if node is not in list
    def remove(self, node:DoubleListNode) -> None:
        pass

    # used so len() can tell you how many items are in the list
    def __len__(self) -> int:
        pass

    # returns the first occurrence of value after start_node
    # raise ValueError if node is not in list
    def find_after(self, value, start_node:DoubleListNode = None) -> DoubleListNode:
        pass

    # returns the last occurrence of value before start_node
    # raise ValueError if node is not in list
    def find_last(self, value, start_node:DoubleListNode = None) -> DoubleListNode:
        pass

    # empties the list
    def clear(self):
        pass