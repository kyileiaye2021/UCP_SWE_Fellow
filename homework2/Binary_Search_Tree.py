# Uber Career Prep 
# Homework 2
# Problem 3 - Binary Search Tree

# For this problem, i need to look up the deletion portion and I am not sure why printing nodes after deletion is not working
class Node:
     def __init__(self, data, left=None, right=None):
         self.data = data
         self.left = left
         self.right = right
         
         
class BinarySearchTree:
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    # returns the minimum value in the BST.  O(logn) time.
    def min(self):
        if not self.root:
            return 0
        curr = self.root
        while curr.left:
            curr = curr.left
            
        return curr.data
    
    # returns the maximum value in the BST.  O(logn) dtime.
    def max(self):
        if not self.root:
            return 0
        
        curr = self.root
        while curr.right:
            curr = curr.right
            
        return curr.data
    
    # returns a boolean indicating whether val is present in the  BST.  O(logn) time.
    def contains(self, val):
        
        if not self.root:
            return False
        
        curr = self.root
        while curr:
            if curr.data > val:
                curr = curr.left
                
            elif curr.data < val:
                curr = curr.right
                
            else:
                return True
            
        return False
    
    # creates a new Node with data val in the appropriate location.   
    def insert(self, val):
        new_node = Node(val)
        
        # if the tree is empty
        if not self.root:
            self.root = new_node
            return
            
        curr = self.root
        parent = None
        
        while curr:
            parent = curr
            if curr.data > val:
                curr = curr.left
                
            elif curr.data < val:
                curr = curr.right
                
            else:  # if the node already exists
                return 
        
        # insertiing the node at the end
        if parent.data > val:
            parent.left = new_node
            
        else:
            parent.right = new_node
            
    # # deletes the Node with data val, if it exists. O(logn) time.
    def find_successor(self, root):
        curr = root
        while curr.left:
            curr = curr.left
            
        return curr
    
    def delete_helper(self,root, val):
        if not root:
            return None
        
        if root.data > val:
            root.left = self.delete_helper(root.left, val)
        elif root.data < val:
            root.right = self.delete_helper(root.right, val)
        
        else: # if the node to be deleted is found
            # delete the leaf node
            if not root.left and not root.right:
                return None
            
            # delete the node that has a single child
            elif not root.left: # has only right child
                return root.right
            
            elif not root.right: # has only left child
                return root.left
            
            # delete the node that has both right and left children
            else: 
                # find min val in right subtree
                successor = self.find_successor(root.right)
                root.data = successor.data
                #remove the successor node
                root.right = self.delete_helper(root.right, successor.data)
            
            return root
        
    def delete(self, val):
        self.root = self.delete_helper(self.root, val)
        
    def inorder_traversal(self, node):
        if not node:
            return None
        self.inorder_traversal(node.left)
        print(node.data, end=" ")
        self.inorder_traversal(node.right)
        
def main():
    root = BinarySearchTree(4)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(8)
    root.insert(7)
    root.insert(9)

    root.inorder_traversal(root.root)
    print()
    print(root.max())  # 9
    print(root.min()) # 3
    print(root.contains(5)) #True
    
    root.delete(3) # removing leave node
    root.inorder_traversal(root.root)
    
    
if __name__ == '__main__':
    main()
    # def delete(self, val):
    #     # delete the node that have both left and right child
        
    #     if not self.root:
    #         return None
        
    #     # search the node in the tree
    #     curr = self.root
    #     parent = None
        
    #     while curr:
    #         parent = curr
    #         if curr.data > val:
    #             curr = curr.left
                
    #         elif curr.data < val:
    #             curr = curr.right
            
    #         else: # if the curr node data is the same as the val
    #             break
        
    #     # delete the leaf node
    #     if not curr.left and not curr.right:
    #         parent.left = None
    #         parent.right = None
        
    #     # delete the node that has a single child
    #     elif curr.left and not curr.right:
    #         parent.left = curr.left
            
    #     elif curr.right and not curr.left:
    #         parent.right = curr.right
            
    #     else: # if the node has both children
            
    #         # find the inorder successor
    #         successor_parent = curr
    #         successor = curr.right
    #         while successor and successor.left:
    #             successor_parent = successor
    #             successor = successor.left # get the leftmost node of the right subtree
            
    #         # copy the successor val to the curr node
    #         curr.data = successor.data
            
    #         # remove the successor node
    #         successor_parent.left = None
            
                
                
            