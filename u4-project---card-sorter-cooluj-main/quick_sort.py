from typing import Dict, List

# quick_sort: IN-PLACE Quick Sort that takes a list of clash cards and sorts them based on the sort key.
# Stores results into the original cards list. You should NOT be creating new lists in this process. 
# Create a recursive version of this function with extra parameters for the indexes you need. 
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorts in place


def quick_sort(cards:List[Dict], sort_key: str)->None: 
    #gets the length of the list of cards
    n = len(cards)
    #Call the sort function, 
    #passing it a list of cards with a starting index of 0 
    #and an ending index of n-1 as well as the sort key.
    sort(cards, 0, n-1, sort_key)
    #sorts the whole array of cards from an index of 0 to the final index by using a (n-1). 
    #The recursive function will use this as its starting point to divide the list into smaller chunks to sort and merge them together.


#creates a function named "partition" with the string "sort key," "low" and "high," and a list of dictionaries called "cards." 
#An integer is returned by this function.
def partition(cards:List[Dict], low:int, high:int, sort_key:str) -> int:
    #sets the pivot value to the element at the high index of the input cards list,
    #using the value at the sort_key key in the dictionary.
    pivot = cards[high][sort_key]
    #initializes the left pointer to one element before the start of the list.
    i = low - 1


    #loop through list, 
    #check if current element is smaller than pivot element
    for j in range(low, high):
        # if the current elements are smaller than pivot element
        if cards[j][sort_key] < pivot:
            i += 1
            # temp value stored so when value is changed, 
            # other value swapped with the store value
            temp = cards[i]
            #swaps the elemts elements
            cards[i] = cards[j] 
            cards[j] = temp
        #stores the current element in a temp value
        temp = cards[i + 1] 
    cards[i + 1] = cards[high]
    cards[high] = temp

    return i+1
    

#this function takes in a list of dictionaries representing cards, 
#two integers representing the lower and higher indexes for the list of cards,
#and a string representing the sort key. It returns nothing.
def sort(cards:List[Dict], low:int, high:int, sort_key:str) -> None:
    #if the lower index is higher than the higher idex the partition list and card 
    if low < high:
        pivot = partition(cards, low, high, sort_key)
        sort(cards, low, pivot-1, sort_key)
        sort(cards, pivot+1, high, sort_key)



