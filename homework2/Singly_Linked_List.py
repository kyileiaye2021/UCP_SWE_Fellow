# Uber Career Prep 
# Homework 2
# Problem 1 - Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Node insertAtFront(Node head, int val) // creates new Node with data val at front; returns head. O(1) time.
def insertAtFront(head, val):
    # create a new node
    # set next node of new node to head next node
    # set head next to new node
    # return head
    new_node = Node(val)
    new_node.next = head.next
    head.next = new_node
    return head
    
# Node insertAtBack(Node head int val) // creates new Node with data val at end; returns head. O(n) time.
def insertAtBack(head, val):
    # create a new node
    # if the node is empty, add the node to the head next
    # set curr to head
    # traverse the list until the curr reaches to the last node
    # set last node next to new node
    new_node = Node(val)
    
    # if the list is empty
    if not head:
        head.next = new_node
        return head
    
    curr = head
    while curr.next:
        curr = curr.next 
        
    curr.next = new_node
    return head

# Node insertAfter(Node head, int val, Node loc) // creates new Node with data val after Node loc; returns head. O(1) time.
def insertAfter(head, val, loc):
    # create a new node
    # if the node is empty, return None
    # set curr to head
    # traverse the list until the curr node is the same as loc node and curr is not none
    #   curr = curr.next
    # set curr.next to new node
    # return head    
    new_node = Node(val)
    
    if not head:
        return None
    
    curr = head
    while curr and curr != loc:
        curr = curr.next
        
    if curr: # if curr is not none
        new_node.next = curr.next
        curr.next = new_node
        return head
    else: # loc node is not in the list
        return None
    
    
# Node insertBefore(Node head, int val, Node loc) // creates new Node with data val before Node loc; returns head. O(n) time.
def insertBefore(head, val, loc):
    # create a new node
    # if the list is empty, return none
    # set curr to head
    # set prev to None to maintain the prev node of the curr
    # travese the list until curr not equal to loc or it becomes None
    # if curr is none: 
    #   return none (there is no loc node in the list
    # else: 
    #   set the next of new node to curr
    # set the next of prev to the new_node
    
    new_node = Node(val)
    if not head:
        return None
    
    if loc == head:
        new_node.next = head
        return new_node
    
    curr = head
    prev = None
    while curr and curr != loc:
        prev = curr
        curr = curr.next
        
    if not curr: # if there is no loc node in the lst, return None
        return None
    else:
        
        new_node.next = curr
        prev.next  = new_node
        return head
        
# Node deleteFront(Node head) // removes first Node; returns head. O(1) time.
def deleteFront(head):
    # if the list is empty
    # return none
    # delete the head node

    if not head:
        return None
    head = head.next
    return head

# Node deleteBack(Node head) // removes last Node; returns head. O(n) time.
def deleteBack(head):
    # if the list is empty
    # traverse the list until the second to last node
    if not head:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = curr.next.next
    return head
    
# Node deleteNode(Node head, Node loc) // deletes Node loc; returns head. O(n) time.
def deleteNode(head, loc):
    # if the list is empty, return none
    # set curr to head
    # set prev to none to maintain prev node of the curr
    # traverse the list until the curr found the log and curr is not none
    # if the curr node is none, return None (no log in the list)
    # else: set prev.next to the curr.next to skip the loc node
    if not head:
        return None
    
    if loc == head:
        head = head.next
        
    curr = head
    prev = None
    while curr and curr != loc:
        prev = curr
        curr = curr.next
        
    if not curr: # if loc node doesn't exist in the list
        return None
    else:
        prev.next = curr.next
    return head

# int length(Node head) // returns length of the list. O(n) time.
def length(head):
    # initialize the counter to 0
    # set curr to head
    # traverse the list until curr becomes none
    # in each traversal, increment the counter
    
    counter = 0
    if not head:
        return counter
    
    curr = head
    while curr:
        curr = curr.next
        counter += 1
    
    return counter

# Node reverseIterative(Node head) // reverses the linked list iteratively. O(n) time.
def reverseIterative(head):
    # set prev to none
    # set curr to head
    # traverse the list until curr reaches to none
    # in each traversal, 
    #   identify the next node
    #   set the next of next node to the curr node
    #   set prev to curr 
    #   set curr to next node
    # return the prev node
    
    prev = None
    curr = head
    while curr:
        next_node = curr.next 
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

# Node reverseRecursive(Node head) // reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
def reverseHelper(head, prev):
    # base case
    # if the list is empty or the curr node becomes none
    #   return
    
    # curr node = head
    # set curr.next to prev
    # call the recursive function with next node of the curr node and setting curr node as prev node
    # return reverseHelper(head.next, curr node)
    
    if not head: # base case
        return head
    
    curr = head
    curr.next = prev
    return reverseHelper(head.next, curr)

def reverseRecursive(head):
    return reverseHelper(head, None) # call helper function

def print_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data)
        curr = curr.next
        
def main():
    n = Node(2) # 2
    loc = n
    n = insertAfter(n,3,loc) # 2 -> 3
    print_list(n)

    n = insertBefore(n,1,loc) # 1 -> 2 -> 3
    print_list(n)
    
    n = insertAtBack(n,4) # 1 -> 2 -> 3 -> 4
    print_list(n) # 1 -> 2 -> 3 -> 4
    
    n = deleteFront(n) # 2 -> 3 -> 4
    print_list(n)
    
    n = deleteBack(n) # 2 -> 3
    print_list(n)
    
    loc = loc.next
    n = deleteNode(n, loc) # 2
    print_list(n) # 2
    
if __name__ == "__main__":
    main()