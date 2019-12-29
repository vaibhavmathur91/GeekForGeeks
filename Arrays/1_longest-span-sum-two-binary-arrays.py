"""
Longest Span with same Sum in two Binary arrays
Given two binary arrays arr1[] and arr2[] of same size n.
Find length of the longest common span (i, j) where j >= i
    such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].

Note: Expected time complexity is Θ(n).

Examples :
    Input: arr1[] = {0, 1, 0, 0, 0, 0};
           arr2[] = {1, 0, 1, 0, 0, 1};
    Output: 4
    The longest span with same sum is from index 1 to 4.

    Input: arr1[] = {0, 1, 0, 1, 1, 1, 1};
           arr2[] = {1, 1, 1, 1, 1, 0, 1};
    Output: 6
    The longest span with same sum is from index 1 to 6.

"""


def longest_common_sum(arr_1, arr_2, arr_len):
    res_len = 0
    pre_sum_1 = 0
    pre_sum_2 = 0
    check_map = {}
    for i in range(arr_len):
        pre_sum_1 += arr_1[i]
        pre_sum_2 += arr_2[i]
        cur_diff = pre_sum_1 - pre_sum_2
        if cur_diff == 0:
            res_len = i+1
        elif cur_diff not in check_map:
            check_map[cur_diff] = i
        else:
            res_len = max(res_len, i - check_map[cur_diff])
    return res_len


# Test1  Ans=4
array_1 = [0, 1, 0, 0, 0, 0]
array_2 = [1, 0, 1, 0, 0, 1]
array_len = len(array_1)
print("\nLength of the longest common span with same sum is", longest_common_sum(array_1, array_2, array_len))

# Test2  Ans=6
array_1 = [0, 1, 0, 1, 1, 1, 1]
array_2 = [1, 1, 1, 1, 1, 0, 1]
array_len = len(array_1)
print("Length of the longest common span with same sum is", longest_common_sum(array_1, array_2, array_len))

# Test3  Ans=0
array_1 = [0, 0, 0]
array_2 = [1, 1, 1]
array_len = len(array_1)
print("Length of the longest common span with same sum is", longest_common_sum(array_1, array_2, array_len))

# Test4  Ans=1
array_1 = [0, 0, 1, 0]
array_2 = [1, 1, 1, 1]
array_len = len(array_1)
print("Length of the longest common span with same sum is", longest_common_sum(array_1, array_2, array_len))
