"""
Find the Number Occurring Odd Number of Times
Given an array of positive integers.
All numbers occur even number of times except one number which occurs odd number of times.
Find the number in O(n) time & constant space.

Examples :
    Input : arr = {1, 2, 3, 2, 3, 1, 3}
    Output : 3

    Input : arr = {5, 7, 2, 7, 5, 2, 5}
    Output : 5
"""


def get_odd_number(arr, n):
    num = arr[0]
    for i in range(1, n):
        num = num ^ arr[i]
    return num


array = [1, 2, 3, 2, 3, 1, 3]
print(get_odd_number(array, len(array)))

array = [5, 7, 2, 7, 5, 2, 5]
print(get_odd_number(array, len(array)))
