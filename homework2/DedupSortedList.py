# Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

# ~ 17 mins
# input:
# 1 -> 2 -> 2 -> 4 -> 5 -> 5 -> 5 -> 10 -> 10
# output: 1 -> 2 -> 4 -> 5 -> 10

# input: 1 -> 1 -> 1 -> 1
# output: 1

# input: 1 -> 2 -> 3 -> 4
# output: 1 -> 2 -> 3 -> 4

# input: 2
# output: 2

# input: NOne
# output: None

# check if the head is none 
#   return none
# set curr to head of the list
# traverse the list until curr reaches the second to last node
#   set next_node to curr.next
#   check if the curr data is = to next node data
#       link the curr next to the next node.next
#   else:
#       move the curr to the curr.next
# return head

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def DedupSortedList(head):
    if not head:
        return None

    curr = head
    while curr.next:
        next_node = curr.next 
        if curr.data == next_node.data:
            curr.next = next_node.next 
            
        else:
            curr = curr.next 
        
    return head

def print_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data)
        curr = curr.next
        
def main():
    list1 = Node(1, Node(2, Node(2, Node(4, Node(5, Node(5, Node(5, Node(10, Node(10)))))))))
    list1 = DedupSortedList(list1)
    print_list(list1)
    
    list2 = Node(1, Node(1, Node(1, Node(1))))
    list2 = DedupSortedList(list2)
    print_list(list2)
    
    list3 = Node(1, Node(2, Node(3, Node(4))))
    list3 = DedupSortedList(list3)
    print_list(list3)
    
    list4 = Node(6)
    list4 = DedupSortedList(list4)
    print_list(list4)
    
    list5 = Node(None)
    list5 = DedupSortedList(list5)
    print_list(list5)
    
if __name__ == '__main__':
    main()
    
# Time complexity - O(n)
# Space complexity - O(1)
