'''
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.
Input Array: [4, 5, -3, 2, 6, 1]
Input k = 2
Output: 4.5

Input Array: [4, 5, -3, 2, 6, 1]
Input k = 3
Output: 3

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1]
Input k = 3
Output: 1

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
Input k = 5
Output: 1
'''

# Happy case
# input: arr- [4, 5, -3, 2, 6, 1], k = 2
# output: 4.5

# input: arr - [1, 1, 1, 1, -1, -1, 2, -1, -1, 6], k = 5
# output - 1

# Edge case
# intput: arr - [1,1,2,-1], k = 4
# output: 1

# Brute Force Approach (nested loop - O(n^k))
# Sliding Window (O(n))

# first operate on the first k ele and find the max mean in first k ele
# itereate over the list from 2nd ele to 2nd to last ele
#   exclude the trailing pointer ele 
#   add the leading pointer ele
#   compute the mean val (curr mean val)
#   update the max mean val if curr mean is greater than max mean val

def max_mean(arr, k):
    
    max_mean_val = float('-inf')
    curr_sum = 0
    
    for i in range(k):
        curr_sum += arr[i]
        max_mean_val = curr_sum / k
        
    for i in range(1, len(arr) - k + 1):
        curr_sum = curr_sum - arr[i - 1]
        curr_sum += arr[i + k - 1]
        curr_mean = curr_sum / k
        max_mean_val = max(max_mean_val, curr_mean)
        
    return max_mean_val
    
# main()
arr = [4, 5, -3, 2, 6, 1]
k = 2 
print(max_mean(arr, k)) # 4.5

arr = [4, 5, -3, 2, 6, 1]
k = 3
print(max_mean(arr,k)) # 3

arr = [1, 1, 1, 1, -1, -1, 2, -1, -1]
k = 3
print(max_mean(arr,k)) #1

arr = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k = 5
print(max_mean(arr,k)) #1

# Time Complexity - O(n)
# Space Complexity - O(1)
# TIme taken ~ 30mins