"""
Find the Missing Number
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list.
One of the integers is missing in the list. Write an efficient code to find the missing integer.

Example :
    Input: arr[] = {1, 2, 4,, 6, 3, 7, 8}
    Output: 5

    Input: arr[] = {1, 2, 3, 5}
    Output: 4
"""


def find_missing_method1(array, array_len):
    total = 1
    for i in range(2, array_len):
        total += i
        total -= array[i-2]
    return total


def find_missing_method2(array, array_len):
    res_given = array[0]
    for i in range(1, array_len):
        res_given = res_given ^ array[i]
    res_original = 1
    for i in range(2, array_len+2):
        res_original = res_original ^ i
    return res_original ^ res_given


# Test1  Ans = 5
array = [1, 2, 4, 6, 3, 7, 8]
array_len = len(array)
print("\n(method1) Missing number is", find_missing_method1(array, array_len))
print("(method2) Missing number is", find_missing_method2(array, array_len))

# Test2  Ans = 4
array = [1, 2, 3, 5, 6]
array_len = len(array)
print("\n(method1) Missing number is", find_missing_method1(array, array_len))
print("(method2) Missing number is", find_missing_method2(array, array_len))
