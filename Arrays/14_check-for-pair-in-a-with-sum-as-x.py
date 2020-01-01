"""
Given an array A[] and a number x, check for pair in A[] with sum as x
Write a program that, given an array A[] of n numbers and another number x,
determines whether or not there exist two elements in S whose sum is exactly x.
"""


def get_pair_sum(arr, n, k):
    check_map = {}
    for i in range(n):
        if k - arr[i] in check_map:
            return True
        else:
            check_map[arr[i]] = True
    return False


array = [1, 4, 45, 6, 10, -8]
x = 16
print(get_pair_sum(array, len(array), x))

array = [5, 7, 2, 7, 5, 2, 5]
x = 10
print(get_pair_sum(array, len(array), x))

array = [4, 5]
x = 1
print(get_pair_sum(array, len(array), x))
