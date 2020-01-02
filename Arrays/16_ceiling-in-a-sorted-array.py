"""
Ceiling in a sorted array
Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.

Examples :

For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array
"""


def get_ceil_element(arr, low, high, k):
    if k <= arr[low]:
        return low
    if k > arr[high]:
        return -1
    mid = (low + high) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] < k:
        if mid + 1 <= high and arr[mid+1] >= k:
            return mid + 1
        else:
            return get_ceil_element(arr, mid+1, high, k)
    else:
        if mid-1 >= low and arr[mid-1] < k:
            return mid
        return get_ceil_element(arr, low, mid-1, k)


array = [1, 4, 7, 16, 20, 45]
x = 16
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [2, 2, 5, 7, 19, 20, 20, 50]
x = 10
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [4, 5]
x = 1
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [1, 2, 8, 10, 10, 12, 19]
x = 20
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [1, 2, 8, 10, 10, 12, 19]
x = 0
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [1, 2, 8, 10, 10, 12, 19]
x = 1
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [1, 2, 8, 10, 10, 12, 19]
x = 5
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))

array = [1, 2, 8, 10, 10, 12, 19]
x = 20
index = (get_ceil_element(array, 0, len(array)-1, x))
if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, array[index]))
