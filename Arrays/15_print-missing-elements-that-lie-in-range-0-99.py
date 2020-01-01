"""
Print missing elements that lie in range 0 – 99
Given an array of integers print the missing elements that lie in range 0-99.
If there are more than one missing, collate them, otherwise just print the number.
Note that the input array may not be sorted and may contain numbers outside the range [0-99],
but only this range is to be considered for printing missing elements.

Examples :
    Input: {88, 105, 3, 2, 200, 0, 10}
    Output: 1
            4-9
            11-87
            89-99

    Input: {9, 6, 900, 850, 5, 90, 100, 99}
    Output: 0-4
            7-8
            10-89
            91-98
"""

LIMIT = 100


def get_pythagorean_triplet(arr, n):
    seen = {i: False for i in range(LIMIT)}
    for i in arr:
        seen[i] = True
    i = 0
    while i < LIMIT:
        if seen[i] is False:
            j = i+1
            while j < LIMIT and seen[j] is False:
                j += 1
            if i+1 == j:
                print(i)
            else:
                print(i, j-1)
            i = j
        else:
            i += 1


array = [88, 105, 3, 2, 200, 0, 10]
get_pythagorean_triplet(array, len(array))
print()
array = [5, 7, 24, 56, 77, 90]
get_pythagorean_triplet(array, len(array))
print()
array = [9, 6, 900, 850, 5, 90, 100, 99]
get_pythagorean_triplet(array, len(array))
print()
