"""
Intersection of two sorted arrays
Given two sorted arrays, find their intersection.

Example:
    Input : arr1[] = {1, 3, 4, 5, 7}
            arr2[] = {2, 3, 5, 6}
    Output : Intersection : {3, 5}

    Input : arr1[] = {2, 5, 6}
            arr2[] = {4, 6, 8, 10}
    Output : Intersection : {6}
"""


def find_intersection(arr_1, arr_2, arr_len):
    i = 0
    j = 0
    res = []
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            i += 1
        elif arr_1[i] > arr_2[j]:
            j += 1
        else:
            res.append(arr_1[i])
            i += 1
            j += 1
    return res


# Test1  Ans= 3 5
array_1 = [1, 3, 4, 5, 7]
array_2 = [2, 3, 5, 6]
array_len = len(array_1)
print("\n Intersection is is", *find_intersection(array_1, array_2, array_len))

# Test2  Ans= 2 5 9 10
array_1 = [2, 5, 6, 7, 8, 9, 10, 11]
array_2 = [2, 3, 5, 9, 10]
array_len = len(array_1)
print("\n Intersection is is", *find_intersection(array_1, array_2, array_len))
