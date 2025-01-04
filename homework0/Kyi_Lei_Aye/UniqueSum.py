# Given an array of integers, return the sum of unique elements in the array.

# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 33 (1+10+8+3+2+5+7+-2+-1)

# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 35 (4+3+5+7+0+2+8+6)

# initialize a set container to store the visited elements
# declare a var to keep track of the total 
# iterate over each ele in the list
#   check if the curr ele is not in the set container
#      update the total by adding the curr ele 
# return total

# Time complexity - O(n)
# Space complexity - O(n)

def unique_sum(list):
    visited = set()
    total = 0

    for ele in list:
        if ele not in visited:
            total += ele
            visited.add(ele)
            
    return total

def main():
    list1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    print(unique_sum(list1)) #33
    
    list2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(unique_sum(list2)) #35
    
main()

# Time spent - 7mins