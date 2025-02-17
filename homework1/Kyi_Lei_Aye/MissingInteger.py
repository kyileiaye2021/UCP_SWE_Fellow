'''
Question 6: MissingInteger
Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

Examples:
Input Array: [1, 2, 3, 4, 6, 7]
Input n: 7
Output: 5

Input Array: [1]
Input n: 2
Output: 2

Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
Input n: 12
Output: 9

'''

# Happy case
# input - arr: [1, 2, 3, 5], n = 5
# output: 4

# Edge case
# input - arr: [1], n = 2
# output: 2

# input - arr: [1,3], n = 3
# output: 2

# input - arr: [1,2], n = 3
# output: 3

# input - arr: [1,3,4], n = 4

# One Pass Iterative Approach (O(n)) - iterate thru the list and compare the curr ele is 1 greater than the prev ele

def missing_integer(array, n):
    for i in range(n-1):
        if array[i] != i + 1:
            return i + 1
    return array[-1] + 1

array =[1, 2, 3, 4, 6, 7]
n = 7
print(missing_integer(array, n)) #5

array = [1]
n = 2
print(missing_integer(array, n)) #2

array = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
n = 12
print(missing_integer(array, n)) #9

#Time - O(n)
# Space - O(1)
# Time taken ~ 12mins
# -----------------------------------------------------------------------

# Optimal way  ?         
# the array is sorted. Possible to use binary search ?
# Forward backward Two pointer approach 

# l, r pointers 
# while l < r
#   check if sum of l ele and r ele is n+1
#       increment l and decrement r
#   else
#       check if l is 1st and r is last ele
#           if l ele not = 1: return 1
#           else: return n
#       check if the difference between curr l and l-1 ele is greater than 1
#           return curr l ele - 1
#       else:
#           return curr r ele + 1

def missing_integer(array, n):
    l, r = 0, len(array) - 1
    
    while l <= r:
        if array[r] + array[l] == n + 1:
            l += 1
            r -= 1
            
        else: 
            if l == 0 and array[l] != 1:
                return 1
            elif r == len(array) - 1 and array[r] != n - 1:
                return n - 1
            else:
                if array[l] - array[l - 1] > 1:
                    return array[l] - 1
                else:
                    return array[r] + 1
                
    return array[-1] + 1

array =[1, 2, 3, 4, 6, 7]
n = 7
print(missing_integer(array, n)) #5

array = [1]
n = 2
print(missing_integer(array, n)) #2

array = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
n = 12
print(missing_integer(array, n)) #9
# Time complexity - log(n)
# Space complexity - O(1)
# Time taken ~ 45 mins