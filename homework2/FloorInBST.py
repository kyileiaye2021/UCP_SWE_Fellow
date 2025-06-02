# Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.
# input: target=13,
#       10
#      /  \
#     8    16
#      \   / \
#       9 13  17
#               \
#               20
# output: 13

# input: target = 15
#       10
#      /  \
#     8    16
#      \   / \
#       9 13  17
#               \
#               20
# output: 13

# DFS
# helper func: max_val
# base case
# if the root is none: return none
# recursive case
# check if the root data is not greater than the target 
#   update max(max_val, root data)
# call on the left subtree
# call on the right subtree
# return the max value among left and right subtree

class Node:
     def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right
         
def FloorInBST_helper(root, max_val, target):
    # base case
    if not root:
        return max_val
    
    # check if the target val is greater than the curr
    # go to the right
    if root.data == target:
        return root.data
    
    elif root.data < target:
        max_val = root.data
        return FloorInBST_helper(root.right, max_val, target)
    
    else:
        return FloorInBST_helper(root.left, max_val, target)
        
    
    # else: go to the left
    
    # if root.data <= target:
    #     max_val = max(max_val, root.data)
    
    # left = FloorInBST_helper(root.left, max_val, target)
    # right = FloorInBST_helper(root.right, max_val, target)
    # return max(left, right, max_val)

def FloorInBST(root, target):
    if not root:
        return None
    return FloorInBST_helper(root, float('-inf'), target)
    
def main():
    root = Node(10)
    root.left = Node(8)
    root.right = Node(16)
    root.left.right = Node(9)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.right.right = Node(20)
    
    target1 = 13
    output1 = FloorInBST(root, target1)
    print(output1) # 13
    
    target2 = 15
    output2 = FloorInBST(root, target2)
    print(output2) # 13
    
    target3 = 18
    output3 = FloorInBST(root, target3)
    print(output3) #17
    
    target4 = 0
    output4 = FloorInBST(root, target4)
    print(output4) # -inf
    
    root2 = None
    output5 = FloorInBST(root2, target4)
    print(output5) # None
    
if __name__ == "__main__":
    main()
    
# Time complexity - O(h)
# Space complexity - O(h)
# Time taken - 45mins