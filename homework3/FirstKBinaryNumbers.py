'''
Given a number, k, return an array of the first k binary numbers, represented as strings.

Examples:
Input: 5
Output: ["0", "1", "10", "11", "100"]

Input: 10
Output: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]

'''

# input - int
# a list of strings

# happy cases
# input = 5
# output = ["0", "1", "10", "11", "100"]

# input = 2
# output = ["0", "1", "10"]

# edge cases
# input = 0
# output = ['0']

# input = -1
# output = []

# res to store the strs
# iterate k times
#   convert the curr ele to binary number
#   for each ele
#      need a deque
#       - divide until the remainder is 1
#       - in each division, add the remainder from the front of the deque
#       - after creating str, add it to the res list
from collections import deque
def k_binary_nums(k):
    res = []
    
    if k < 0:
        return res
    if k == 0:
        res.append('0')
    
    for i in range(k):
        curr_ele = i
        curr_binary = ""
        
        while curr_ele // 2 != 0:
            curr_binary += (f"{curr_ele % 2}")
            curr_ele = curr_ele // 2
        curr_binary += (f"{curr_ele % 2}")
        curr_binary = curr_binary[: : -1]
        res.append(curr_binary)
        
    return res

def main():
    k1 = 5
    print(f"k = {k1}: {k_binary_nums(k1)}\n") # ["0", "1", "10", "11", "100"]
    k2 = 10
    print(f"k = {k2}: {k_binary_nums(k2)}\n") # ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
    k3 = 25
    print(f"k = {k3}: {k_binary_nums(k3)}\n")
    k4 = 0
    print(f"k = {k4}: {k_binary_nums(k4)}\n") # ['0']
    k5 = -5
    print(f"k = {k5}: {k_binary_nums(k5)}\n") # []          
            
if __name__ == '__main__':
    main()
    
# time complexity - O(k)
# space complexity - O(k)
# Time taken - ~20mins
# At first, I don't know how to solve this problem, and then I remember I learned how to convert decimal to binary nums in computer organization class!