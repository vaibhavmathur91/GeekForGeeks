"""
Leaders in an array
Write a program to print all the LEADERS in the array.
An element is leader if it is greater than all the elements to its right side.
And the rightmost element is always a leader.
For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

Examples :
    Input : {16, 17, 4, 3, 5, 2}
    Output : 17 5 2
"""


def print_leaders(arr, n):
    max_left = float("-inf")
    for i in range(n-1, -1, -1):
        if arr[i] > max_left:
            print(arr[i], end=" ")
            max_left = arr[i]


array = [16, 17, 4, 3, 5, 2]
print_leaders(array, len(array))
