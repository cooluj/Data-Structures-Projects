from typing import Dict, List

# merge_sort: takes a list of clash cards and sorts them based on the sort key.
# Merges results into the original cards list
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorted results are stored directly in cards
def merge_sort(cards: List[Dict], sort_key: str)->None:
    #this is the base and if there is only one card in the list it will have nothing to sort
    if len(cards) <= 1:
        return

    middle = len(cards) // 2
    #create two new lists with the values from the original list, split at the middle index
    left = []
    for i in range(0, middle):
        left.append(cards[i])
    right = []
    for i in range(middle,len(cards)):
        right.append(cards[i])

    #recursively calls merge_sort on both of the new lists
    merge_sort(left, sort_key)
    merge_sort(right, sort_key)

    #initializes pointers to keep track of the list
    left_pointer = 0
    right_pointer = 0

    #compares the "left" and "right" lists to determine if is within the bounds of their respective lists
    # and checks if both the left and right pointers are less than the length of their  lists,
    # if there are still elements in the lists are not processed. 
    # This line is used in a loop and will continue until left or right list has processed.
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer][sort_key] < right[right_pointer][sort_key]:
            
            cards[left_pointer + right_pointer] = left[left_pointer]
            left_pointer += 1
        else:
            cards[left_pointer + right_pointer] = right[right_pointer]
            #moves pointer
            right_pointer += 1
    #continue as long as the left_pointer is less than the length of the left list.
    #it merges the two sorted lists together while and keeps track of the current position in the left list.
    while left_pointer < len(left):
        cards[left_pointer + right_pointer] = left[left_pointer]
        left_pointer += 1

    #continue as long as the right_pointer is less than the length of the right list.
    #it merge the two sorted lists together while and keeps track of the current position in the right list.
    while right_pointer < len(right):
        cards[left_pointer + right_pointer] = right[right_pointer]
        right_pointer += 1
