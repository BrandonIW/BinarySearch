# With binary search algorithms, this is a method to search an ordered list of data, but instead of searching
# one value at a time, we divide and conquer. We start with the middle value and see if that middle value of lower
# or higher than that value we're searching for. Then we can ignore half the list. Then we repeat this. However this
# depends on that list being sorted in some way

# In contrast, a naive search will scan the elements one at a time in a list and ask "is this it" "is this it" etc. It's
# a "dumb" search

import time
from random import randint

def naive_search(list,target):

    for idex in range(len(list)):
        if list[idex] == target:
            stop = time.time()
            return idex
    return -1


def binary_search(list,target,low=None,high=None):
    if low is None:
        low = 0

    if high is None:
        high = len(list) - 1

    if high < low:                       # The target is not in the list if high is every lower than low
        return -1

    midpoint = (low+high) // 2            # Division but integer rounding. Does not return a float.


    if list[midpoint] == target:            # If the list at index 'midpoint' is the target, then return it
        return midpoint

    elif target < list[midpoint]:
        return binary_search(list,target,low,midpoint-1)

    elif target > list[midpoint]:
        return binary_search(list,target,midpoint+1,high)

if __name__ == "__main__":
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(randint(-3*length,3*length))     # Create a sorted list of a random 10000 number list of sorted numbers
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    naive_search(sorted_list,4523)
    stop = time.time()
    print(f"This took {stop-start} seconds")

    start = time.time()
    binary_search(sorted_list, 4523)
    stop = time.time()
    print(f"This took {stop-start} seconds")
