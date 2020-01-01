"""
Pythagorean Triplet in an array
Given an array of integers,
write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Example:
    Input: arr[] = {3, 1, 4, 6, 5}
    Output: True  There is a Pythagorean triplet (3, 4, 5).

    Input: arr[] = {10, 4, 6, 12, 5}
    Output: False  There is no Pythagorean triplet.
"""


def get_pythagorean_triplet(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    arr.sort()
    for i in range(n-1, -1, -1):
        j = 0
        k = i-1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1
    return False


array = [16, 17, 4, 3, 5, 2]
print(get_pythagorean_triplet(array, len(array)))

array = [5, 7, 2, 7, 5, 2, 5]
print(get_pythagorean_triplet(array, len(array)))

array = [4, 5]
print(get_pythagorean_triplet(array, len(array)))
