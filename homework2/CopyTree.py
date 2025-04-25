# Question 7: CopyTree
# Given a binary tree, create a deep copy. Return the root of the new tree.

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
    
def copy_tree(root):
    if not root:
        return None
    
    new_node = Node(root.data)
    new_node.left = copy_tree(root.left)
    new_node.right = copy_tree(root.right)
    return new_node
    
def inorder_traversal(root):
    if not root:
        return None
    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)
    
def main():
    root = BinarySearchTree(4)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(8)
    root.insert(7)
    root.insert(9)
    
    copy = copy_tree(root.root)
    inorder_traversal(copy)
    
if __name__ == '__main__':
    main()
    

   
    
    