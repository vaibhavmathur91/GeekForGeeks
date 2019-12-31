"""
Replace every element with the greatest element on right side
Given an array of integers, replace every element with the next greatest element
(greatest element on the right side) in the array. Since there is no element next to the last element,

Example
    Input : arr = {16, 17, 4, 3, 5, 2}
    Output : arr = {17, 5, 5, 5, 2, -1}

"""


def get_replace_every_number_by_right_max(arr, n):
    if arr:
        max_r = arr[-1]
        arr[-1] = -1
        for i in range(n-2, -1, -1):
            temp = max_r
            max_r = max(max_r, arr[i])
            arr[i] = temp
    return arr


array = [16, 17, 4, 3, 5, 2]
print(get_replace_every_number_by_right_max(array, len(array)))

array = [5, 7, 2, 7, 5, 2, 5]
print(get_replace_every_number_by_right_max(array, len(array)))
