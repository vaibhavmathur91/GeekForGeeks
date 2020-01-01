"""
Count Strictly Increasing Sub Arrays
Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing.
Expected Time Complexity : O(n)
Expected Extra Space: O(1)

Examples:
    Input: arr[] = {1, 4, 3}
    Output: 1    There is only one subarray {1, 4}

    Input: arr[] = {1, 2, 3, 4}
    Output: 6  There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4} {2, 3}, {2, 3, 4} and {3, 4}

    Input: arr[] = {1, 2, 2, 4}
    Output: 2    There are 2 subarrays {1, 2} and {2, 4}
"""


def get_strictly_increasing_sub_array(arr, n):
    cur_len = 1
    res = 0
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            cur_len += 1
        else:
            res += (cur_len * (cur_len-1))//2
            cur_len = 1
    if cur_len > 1:
        res += (cur_len * (cur_len - 1)) // 2
    return res


array = [1, 4, 3]
print(get_strictly_increasing_sub_array(array, len(array)))

array = [5, 7, 2, 7, 5, 2, 5]
print(get_strictly_increasing_sub_array(array, len(array)))

array = [1, 2, 3, 4]
print(get_strictly_increasing_sub_array(array, len(array)))

array = [1, 3, 20, 4, 1, 0]
print(get_strictly_increasing_sub_array(array, len(array)))

array = [1, 2, 2, 4]
print(get_strictly_increasing_sub_array(array, len(array)))
