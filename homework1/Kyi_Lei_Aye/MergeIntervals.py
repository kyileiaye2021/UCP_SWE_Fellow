'''

Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

Examples:

Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]

'''

# Happy case
# input: [(1,2), (3,4)]
# output: [(1,2),(3,4)]

# input: [(2,3), (1,2)]
# output: [(1,3)]

# input: [(1,4), (2,3)]
# output: [(1,4)]

# edge case:
# input: [(1,2)]
# output: [(1,2)]

# First Approach: Sort & Compare adjacent tuples in the list

# Sort the list by the first eles in tuples - O(nlogn)
# create a set for the res  
# iterate thru the sorted list from the second tuple
#   check if the first ele in the tuple is greater or equal to first ele in prev tuple and less than or equal to the second ele in prev tuple
#       check if the second ele in the curr tuple is greater than or equal to the second ele in prev tuple
#           put the tuple of (first ele in prev tuple, second ele in curr tuple) in res set
#       else
#           put the tuple of (first ele in prev tuple, second ele in prev tuple) in res set
#   else
#       put the tuple of (first ele in curr tuple, second ele in curr tuple) in the res set
# convert res set to list and return res list


def mergeIntervals(interval_lst):
    res = set()
    
    interval_lst.sort() # sort the list of tuples by first elements in tuples
    print(f"sorted: {interval_lst}")
    for i in range(1, len(interval_lst)):
        
        if interval_lst[i][0] >= interval_lst[i - 1][0] and interval_lst[i][0] <= interval_lst[i - 1][1]: # if overlapped
            
            # for second ele
            if interval_lst[i][1] >= interval_lst[i - 1][1]:
                res.add((interval_lst[i - 1][0], interval_lst[i][1]))
                
            else:
                res.add((interval_lst[i - 1][0], interval_lst[i - 1][1]))
                
        else: # if not overlapped
            res.add(interval_lst[i])
    
    res = list(res)
    return res

input = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(mergeIntervals(input)) # [(4, 8), (1, 3), (9, 12)]

input = [(5, 8), (6, 10), (2, 4), (3, 6)]
print(mergeIntervals(input)) # [(2, 10)]

input = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(mergeIntervals(input)) #[(10, 12), (5, 6), (7, 9), (1, 3)]

# ~ 20mins - understanding questions with happy cases, edge cases, thinking approach, and writing down step by step pseudocodes
# ~ 7mins - writing code
# the second test case is not passed! 

#-----------------------------------------------------------------------------------------

# I tried another way

# Second approach - Sort and Compare with elements in Stack data structures

# I used stack to compare the current tuple in the list and top ele in the stack
# sort the list and check the curr tuple with the top tuple in the stack

def mergeIntervals_stack(interval_lst):
    res = []
    
    interval_lst.sort() # sort the list of tuples by first elements in tuples
    print(f"sorted: {interval_lst}")
    res.append(interval_lst[0])
    
    for i in range(1, len(interval_lst)):
        
        top_tuple = res[-1]
        if interval_lst[i][0] >= top_tuple[0] and interval_lst[i][0] <= top_tuple[1]: # if overlapped
            
            # for second ele in the tuple
            if interval_lst[i][1] >= top_tuple[1]:
                res.pop()
                res.append((top_tuple[0], interval_lst[i][1]))
                
            # else:
            #     res.add((top_tuple[0], top_tuple[1]))
                
        else: # if not overlapped
            res.append(interval_lst[i])
    
    res = list(res)
    return res

input = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(mergeIntervals_stack(input)) # [(4, 8), (1, 3), (9, 12)]

input = [(5, 8), (6, 10), (2, 4), (3, 6)]
print(mergeIntervals_stack(input)) # [(2, 10)]

input = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(mergeIntervals_stack(input)) #[(10, 12), (5, 6), (7, 9), (1, 3)]

# Time complexity - O(nlogn) we are sorting the list before operation
# Space complexity - O(n) we used stack and convert it to list 
# Time Taken
# first approach ~ 30mins
# second approach ~ 15mins
