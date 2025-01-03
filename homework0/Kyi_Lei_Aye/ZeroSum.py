# Question 1: ZeroSum
# Given an array of integers, return the number of pairs of integers in the array that sum to 0 assuming you can use the element at each index at most once.

# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 2
# (Pairs: (1, -1), (2,-2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2,-2), (2,-2))

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 0

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
# Output: 1
# (Pairs: (0, 0))

# Time complexity - O(n)
# Space complexity - O(n)

# create a freq map
# create a counter val to 0 to keep track of the pairs add up to 0
# iterate through the array
#   populate the freq map
# iterate over the array
#   check if the curr ele freq is greater than 0
#       decrement the freq val of curr ele by 1
#       check if the neg ele of curr ele is in freq map
#           increment the counter by 1
#           decrement the freq val of neg ele of curr ele
# return the counter

def zerosum(lst):
    freq = {}
    counter = 0
    for ele in lst:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
    
    for ele in lst:
        if freq[ele] > 0:
            freq[ele] -= 1
            neg_val = 0 - ele
            if neg_val in freq and freq[neg_val] > 0:
                freq[neg_val] -= 1
                counter += 1
                
    return counter

def main():
    lst1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(zerosum(lst1)) # 2
    
    lst2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    print(zerosum(lst2)) # 3
    
    lst3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(zerosum(lst3)) # 0
    
    lst4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
    print(zerosum(lst4)) # 1
    
main()

# Time spent - around 40 mins

# Follow-Up: Now assume you can re-use elements in different pairs (i.e., the elements in a pair must be from different indices but different pairs may use an element form the same index).

# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2,-2), (2,-2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 5
# (Pairs: (1, -1), (2,-2), (2,-2), (2,-2), (2,-2))

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 0

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
# Output: 1
# (Pairs: (0, 0))

# Time complexity - O(n)
# Space complexity - O(n)
def zerosum(lst):
    freq = {}
    counter = 0
    for ele in lst:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
        
    for ele in freq:
        if ele == 0: # i think this condition needs more improvement. 
        # If there are two 0s, the pair num is 1. If there are three 0s, the pair num should be 3.
        # if there are four 0s, the pair num should be 6 i guess.
             counter += freq[ele] // 2
             freq[ele] = 0
        else:
            neg_val = 0 - ele
            if neg_val in freq:
                counter += freq[ele] * freq[neg_val]
                freq[ele] = 0
                freq[neg_val] = 0
                    
    return counter

def main():
    lst1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(zerosum(lst1)) # 3
    
    lst2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    print(zerosum(lst2)) # 5
    
    lst3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(zerosum(lst3)) # 0
    
    lst4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
    print(zerosum(lst4)) # 1
    
main()

# I spent a lot more time on this follow up question but tried my best to solve it.