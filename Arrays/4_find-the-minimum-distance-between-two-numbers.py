"""
Find the minimum distance between two numbers
Given an unsorted array arr[] and two numbers x and y,
find the minimum distance between x and y in arr[].
 The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples:
    Input: arr[] = {1, 2}, x = 1, y = 2
    Output: Minimum distance between 1 and 2 is 1.

    Input: arr[] = {3, 4, 5}, x = 3, y = 5
    Output: Minimum distance between 3 and 5 is 2.

    Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
    Output: Minimum distance between 3 and 6 is 4.
"""


def min_dist(arr, n, x, y):
    first = arr[0]
    res = float("inf")
    for i in range(n):
        if arr[i] == x or arr[i] == y:
            first = arr[i]
            start = i
            break
    cur = start+1
    while cur < n:
        if arr[cur] == x or arr[cur] ==y:
            if arr[cur] == first:
                first = arr[cur]
                start = cur
            else:
                res = min(res, cur-start)
                first = arr[cur]
                start = cur
        cur += 1
    return res


# Test1  Ans=4
array = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
array_len = len(array)
left = 3
right = 6
print("Minimum distance between ", left, " and ", right, "is", min_dist(array, array_len, left, right))

# Test2  Ans=3
array = [3, 5, 4, 2, 6, 5, 6, 6, 4, 8, 3, 7, 5, 6, 7, 7, 7, 8, 89, 67, 4, 3, 3]
array_len = len(array)
left = 5
right = 8
print("Minimum distance between ", left, " and ", right, "is", min_dist(array, array_len, left, right))

# Test3  Ans=6
array = [3, 5, 4, 2, 6, 5, 6, 6, 4, 8, 3, 7, 5, 6, 7, 7, 7, 8, 89, 67, 4, 3, 3]
array_len = len(array)
left = 2
right = 8
print("Minimum distance between ", left, " and ", right, "is", min_dist(array, array_len, left, right))

