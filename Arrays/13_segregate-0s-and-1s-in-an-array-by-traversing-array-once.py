"""
Segregate 0s and 1s in an array
You are given an array of 0s and 1s in random order.
Segregate 0s on left side and 1s on right side of the array. Traverse array only once.

Example:
    Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
"""


def get_separated_array(arr, n):
    i = 0
    j = n - 1
    while i < j:
        if arr[i] == 0:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr


array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(get_separated_array(array, len(array)))

array = [0, 1, 0, 1, 0]
print(get_separated_array(array, len(array)))

array = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1,]
print(get_separated_array(array, len(array)))
