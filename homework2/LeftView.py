# Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

# input: [[7] [8,3] [9, 13] [20,14], [15]]
# output: [7, 8, 9, 20, 15]

# input: [[7] [20,4] [15, 6,8, 11]]
# output: [7,20. 15]

# input: none
# output: none

# input: [[4]]
# output: [4]

# BFS
# create a queue to store ele from each level
# create a res to store the res 
# add the head node to queue
# traverse q until it is empty
#   need to take out the node from q
#   add that very node to the res list
#   check if node has left child
#       add it to the q
#   check if node has right child
#       add it to the q
# return res

class Node:
     def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right
         
def LeftView(root):
    
    if not root:
        return None
    q = []
    res = []
    left_taken_out = False
    q.append(root)
    while q:
        
        len_q = len(q)
        
        for _ in range(len_q):
            node = q.pop(0)
            if not left_taken_out:
                res.append(node.data)
                left_taken_out = True
                
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
            
        left_taken_out = False
    return res
        
def main():
    # Test case 1
    root = Node(7)
    root.left = Node(8)
    root.right = Node(3)
    
    root.right.left = Node(9)
    root.right.right = Node(13)
    
    root.right.left.left = Node(20)
    root.right.right.left = Node(14)
    
    root.right.right.left.right = Node(15)
    
    res = LeftView(root)
    print(res) # [7, 8, 9, 20, 15]
    
    # Test case 2
    root1 = Node(7)
    root1.left = Node(20)
    root1.right = Node(4)
    
    root1.left.left = Node(15)
    root1.left.right = Node(6)
    
    root1.right.left = Node(8)
    root1.right.right = Node(11)
    
    res1 = LeftView(root1)
    print(res1) # [7,20. 15]
    
    # Test case 3
    root2 = Node(4)
    print(LeftView(root2)) #4
    
    # Test case 4
    root3 = None
    print(LeftView(root3)) # None
    
if __name__ == '__main__':
    main()
    
# Time complexity - O(n)
# Space complexity - O(n)
# Time taken - ~20mins