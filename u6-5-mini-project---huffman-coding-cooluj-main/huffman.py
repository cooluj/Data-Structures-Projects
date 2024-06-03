from typing import Dict, Tuple
from huffman_node import HuffmanNode
from pri_queue import PriorityQueue
 
#I got some help from my firends Sam, Vaibhav, and Lucky

class HuffmanCoding:
  
    # encodes a string and returns the huffman tree and the resulting binary sequence
    # as a string
    # Note: to call static methods, type the class name before the call, e.g. HuffmanCoding.encode(...)
    # We are using static methods because functions are self contained and don't need to maintain
    # object state.

    @staticmethod
    def encode(string)->Tuple[Dict[str,str], str]:
        priority_queue = HuffmanCoding._generate_priority_queue(string)
        huffman_tree = HuffmanCoding._generate_huffman_tree(priority_queue)
        char_coding = HuffmanCoding._get_char_codes(huffman_tree)
 
        encoded = ""
        for character in string:
            encoded += char_coding[character]
 
        return huffman_tree, encoded
   
    # takes the huffman tree root and the encoded string and decodes the message
    @staticmethod
    def decode(huffman_tree:HuffmanNode, encoding:str):
        decoded = ""
        current = huffman_tree
        for bit in encoding:
            if bit == "0":
                current = current.left
            elif bit == "1":
                current = current.right
            if current.value:
                decoded += current.value
                current = huffman_tree
        return decoded
 
    ################# SUGGESTED HELPER FUNCTIONS ###################
    # The tests do not depend on these, so modify and use these however you want, or not at all
    ################################################################
   
    # Builds a priority queue from the characters in the input_string, where the priority is
    # based on how many times a character appears. Smaller counts should come off the pqueue first.
    @staticmethod
    def _generate_priority_queue(input_string:str)->PriorityQueue:
        value = {}
        for character in input_string:
            if character not in value:
                value[character] = 1
            else:
                value[character] += 1
        priority_queue = PriorityQueue()
        for character in value:
           node = HuffmanNode(character, value[character])
           priority_queue.enqueue(node.weight, node)
 
        return priority_queue
 
    # Builds a Huffman tree based on a priority queue using the Huffman Algorithm.
    # Dequeue 2 items at a time from the pqueue, put them under a new node, then enqueue the new node.
    # Repeat until you have only 1 node.
    @staticmethod
    def _generate_huffman_tree(priority_queue :PriorityQueue)->HuffmanNode:
        while priority_queue.size() >= 2:
            left = priority_queue.dequeue()
            right = priority_queue.dequeue()
            node = HuffmanNode(None, left.weight + right.weight, left, right)
            priority_queue.enqueue(node.weight, node)
        return priority_queue.dequeue()
 
    # Traverses the Huffman tree to find the binary codes for each character and returns
    # a dictionary of codes for each character
    # Tip: Don't forget to convert your 0s and 1s to strings to concatenate them!
    @staticmethod

    #this will take the Huffman tree root node as input and return as a dict and calls _get_char_codes_ recursive through the tree
    def _get_char_codes(huffman_tree_root:HuffmanNode)->Dict:
        return HuffmanCoding._get_char_codes_recursive(huffman_tree_root, "")
 
    @staticmethod
    def _get_char_codes_recursive(node: HuffmanNode, current_prefix: str) -> Dict[str, str]:
        char_codes = {}
        if node.value:
            char_codes[node.value] = current_prefix
        else:
            char_codes.update(HuffmanCoding._get_char_codes_recursive(node.left, current_prefix + "0"))
            char_codes.update(HuffmanCoding._get_char_codes_recursive(node.right, current_prefix + "1"))
        return char_codes



