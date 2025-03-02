'''
Question 9: DedupArray
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

Examples:
Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Modified Array: [1, 2, 3, 4] 
or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

Input Array: [1, 3, 4, 8, 10, 12]
Modified Array: [1, 3, 4, 8, 10, 12]

'''

# happy cases
# input: [0,1,2,3,3]
# output: [0,1,2,3,-1]

# input: [1,2,5,5,5,6]
# output: [1,2,5,6,-1,-1]

# edge cases
# input: [1,2,3]
# output: [1,2,3]

# input: [0]
# output: [0]

# brute force - create another list and put unique elements in the list and at the end append -1s for the remaining elements [O(n) time and O(n) space]
# Two pointer with reset/ catch up (l, r)
# first both pointing to the second elements in the list 
# l will represent index of unique elements
# r will iterate thru elements in the list
# while r is less than the len of the list
#   check if the r pointer ele is not equal to the prev ele
#       move r pointer ele to the position where the l pointer is currrently pointing to
#       increment l by 1 
#       increment r by 1
#   else: increment r by 1
# for the remaining part of the list, replace the elements with -1s in the list
# return the list

def dedupArray(nums):
    
    l, r = 1,1
    while r < len(nums):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l += 1
        r += 1
        
    while l < len(nums):
        nums[l] = -1
        l += 1
    
    return nums

n = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(dedupArray(n)) #[1, 2, 3, 4] or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

n = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
print(dedupArray(n)) #[0, 1, 4, 5, 8, 9, 10, 11, 15] or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

n = [1, 3, 4, 8, 10, 12]
print(dedupArray(n)) # [1, 3, 4, 8, 10, 12]

# Time complexity - O(n)
# Space complexity -O(1) We are doing it in-place
# ~ 12mins to understand question, think happy case, edge cases, approaches, write step by step pseudocode
# ~ 3mins to write codes and test cases
# Total time - ~15mins