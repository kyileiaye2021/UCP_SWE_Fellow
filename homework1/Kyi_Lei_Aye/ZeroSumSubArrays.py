'''
Question 3: ZeroSumSubArrays
Given an array of integers, count the number of subarrays that sum to zero.

Examples:
Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2
(Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

Input Array: [1, 8, 7, 3, 11, 9]
Output: 0

Input Array: [8, -5, 0, -2, 3, -4]
Output: 2
(Subarrays: [0], [8, -5, 0, -2, 3, -4])

'''

# Happy casess
# input = [1,0,-1]
# output = 1

# input = [4, 5, 2, -1, -3, -3, 4, 6, -7]
# output - 2

# input - [1, 8, 7, 3, 11, 9]
# output - 0

# input - [8, -5, 0, -2, 3, -4]
# output - 2

# Brute Approach (Nested loop to count the num of sub arrays that add up to 0- O(n^2))
# sliding window with variable size
    
# One directional running computation/total
# prefix sum and hashmap
# hashmap: {prefix : freq}
# if prefix sum counts more than 1 -> the subarray between that two prefix sum add up to 0

# create a hashmap
# create a curr_sum to 0
# iterate over the list
#   accumulate curr_sum 
#   accumulate the hashmap

# initialize counter var to 0
# iterate the hashmap
#   check if the val of curr key is greater than 1
#   increment the counter by the amount of that val
# return the counter

def zero_sum_subarray(arr):
    freq = {}
    curr_sum = 0
    counter = 0
    
    for ele in arr:
        curr_sum += ele
        if curr_sum == 0:
            counter += 1
        if curr_sum in freq:
            # freq[curr_sum] += 1
            counter += 1
        else:
            freq[curr_sum] = 1
    
    # for prefix_sum in freq:
    #     if freq[prefix_sum] > 1:
    #         counter += 1
            
    return counter

input = [1,0,-1]
print(zero_sum_subarray(input)) # 2

input = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(zero_sum_subarray(input)) #2

input = [1, 8, 7, 3, 11, 9]
print(zero_sum_subarray(input)) #0

input = [8, -5, 0, -2, 3, -4]
print(zero_sum_subarray(input)) #2

# Time complexity - O(n)
# Space complexity - O(n)
# Time taken ~ 1hr

# In this problem, I learned that we can use hashmap and prefix sum to avoid computing prev window sum.
# Also, i learned that the subarray between the same prefix sum is 0.