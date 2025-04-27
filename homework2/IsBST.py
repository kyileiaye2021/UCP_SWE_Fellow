# Given a binary tree, determine if it is a binary search tree.

#       10
#      /  \
#     8    16
#      \   / \ 
#       9 13 17
#              \
#               20

# True

#       10
#      /  \
#     8    16
#      \   / \ 
#       9 13 17
#              \
#               15
# False (15 is on the right subtree of 16 and 17)

#       10
#      /  \
#     8    16
#      \   / \ 
#       12 13 17
#              \
#               20
# False (12 is in left subtree of 10)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        

def isBST_helper(root, max, min):
    # if the tree is empty
    if not root:
        return True
    
    if root.data <= min or root.data >= max:
        return False
    
    # in the left subtree, the node keys cannot be greater than the curr root node
    left_subtree = isBST_helper(root.left, root.data, min)
    # in the right subtree, the node keys cannot be less than the curr root node
    right_subtree = isBST_helper(root.right, max, root.data)
   
    return left_subtree and right_subtree

def isBST(root):
    if not root:
        return True
    return isBST_helper(root, float('inf'), float('-inf'))

def main():
    root = Node(10)
    root.left = Node(3)
    root.right = Node(12)
    root.right.left = Node(11)
    root.right.right = Node(14)
    
    print(isBST(root)) # True
    
    root.right.right.left = Node(9)
    print(isBST(root)) # False
    
if __name__ == '__main__':
    main()