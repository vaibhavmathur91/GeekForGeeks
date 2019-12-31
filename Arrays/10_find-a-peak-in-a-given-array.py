"""
Find a peak element
Given an array of integers. Find a peak element in it.
An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.

Following corner cases give better idea about the problem.
    1) If input array is sorted in strictly increasing order, the last element is always a peak element.
        For example, 50 is peak element in {10, 20, 30, 40, 50}.
    2) If input array is sorted in strictly decreasing order, the first element is always a peak element.
        100 is the peak element in {100, 80, 60, 50, 20}.
    3) If all elements of input array are same, every element is a peak element.

Examples:
      Input: arr[] = {5, 10, 20, 15}
      Output: 20

      Input: arr[] = {10, 20, 15, 2, 23, 90, 67}
      Output: 20 90 (Note that we need to return any one peak element.)

"""


def get_peak_number(arr, low, high, n):
    mid = int(low + (high - low) / 2)
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return mid
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return get_peak_number(arr, low, (mid - 1), n)
    else:
        return get_peak_number(arr, (mid + 1), high, n)


array = [16, 17, 4, 3, 5, 2]
print(get_peak_number(array, 0, len(array), len(array)))

array = [5, 7, 2, 7, 5, 2, 5]
print(get_peak_number(array, 0, len(array), len(array)))

array = [4, 5]
print(get_peak_number(array, 0, len(array), len(array)))

array = [1, 3, 20, 4, 1, 0]
print(get_peak_number(array, 0, len(array), len(array)))
