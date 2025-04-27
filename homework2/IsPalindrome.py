# Given a doubly linked list, determine if it is a palindrome.

# Happy cases
# input: list = 9->2->4->2->9
# output: True 

# input: list = 9->12>4->2->9
# output: False

# input: list = 2->2
# output: True

# Edge cases
# input: list = 23
# output: False

# input: list = None
# output: False

# input: list = 2->3
# output: False

# traverse the list until the curr reaches end of the list
# set tail to the end
# set curr to head
# traverse the list until curr is equal to tail
#   check if the curr data is equal to the tail data
#       move the tail to tail prev node
#       move the curr to next curr node
#   else: return false
# return true

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
def IsPanlindrome(head):
    
    if not head or not head.next:
        return False
    
    # finding the last node in the list
    tail = head
    while tail.next:
        tail = tail.next
    
    curr = head
    
    while curr != tail:
        if curr.data == tail.data:
            curr = curr.next 
            tail = tail.prev
            
        else:
            return False
        
    return True

def print_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data)
        curr = curr.next
        
def main():
    
     node1 = Node(9)
     node2 = Node(2)
     node3 = Node(4)
     node4 = Node(2)
     node5 = Node(9)
     
     node1.next = node2
     node2.next = node3
     node3.next = node4
     node4.next = node5
     
     node5.prev = node4
     node4.prev = node3
     node3.prev = node2
     node2.prev = node1
     
     list1 = node1
     # Testing happy cases
     print("list: ", end="")
     print_list(list1)
     print("Panlindrome?: ", IsPanlindrome(list1)) # True
     
     node2.data = 12
     print("list: ", end="")
     print_list(list1)
     print("Panlindrome?: ", IsPanlindrome(list1)) # False
     
     node1 = Node(2)
     node2 = Node(2)
     node1.next = node2
     node2.prev = node1
     list2 = node1
     print("list: ", end="")
     print_list(list2)
     print("Panlindrome?: ", IsPanlindrome(list2)) # True
     
     list3 = Node(1)
     print("list: ", end="")
     print_list(list3)
     print("Panlindrome?: ", IsPanlindrome(list3)) # False
     
     list4 = Node(2, Node(3))
     print("list: ", end="")
     print_list(list4)
     print("Panlindrome?: ", IsPanlindrome(list4)) # False
     
     list5 = Node(None)
     print("list: ", end="")
     print_list(list5)
     print("Panlindrome?: ", IsPanlindrome(list5)) # False
if __name__ == '__main__':
    main()
    
# Time = 22mins
# Time complexity - O(n)
# Space complexitu - O(1)