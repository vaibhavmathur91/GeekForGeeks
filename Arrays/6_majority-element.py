"""
Majority Element
Write a function which takes an array and prints the majority element (if it exists),
otherwise prints “No Majority Element”.
A majority element in an array A[] of size n is an element that appears more than n/2 times

Examples :
    Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
    Output : 4

    Input : {3, 3, 4, 2, 4, 4, 2, 4}
    Output : No Majority Element
"""

from _collections import defaultdict


def print_majority_element(arr, n):
    mapper = defaultdict(int)
    for i in arr:
        mapper[i] += 1
    to_print = True
    for k, v in mapper.items():
        if v > n//2:
            print("Majority item is ", k)
            to_print = False
            break
    if to_print:
        print("Not found")


array = [2, 2, 2, 2, 5, 5, 2, 3, 3]
print_majority_element(array, len(array))

array = [2, 5, 3]
print_majority_element(array, len(array))
