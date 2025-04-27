# Given a singly linked list, move the nth from the last element to the front of the list.

# input: k = 2, list = 15->2->8->7->20->9->11->6->19
# output: 6->15->2->8->7->20->9->11->19

# input: k = 7, list = 15->2->8->7->20->9->11->6->19
# output: 8->15->2->7->20->9->11->6->19

# edge cases;
# input: k = 1, list = 5
# output: 5

# input: k = 0, list = None
# output: None

# if the node is None
#   return None
# if the node is only one ele 
#   return head
# set prev to None
# set curr to head
# traverse k times to find the node to be removed
# set temp node to curr
# connect prev.next to curr.next
# connect the temp node.next to the head 
# return temp

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def make_copy(head):
    new_head = Node(0)
    dummy = new_head
    while head:
        new_node = Node(head.data)
        new_head.next = new_node
        new_head = new_head.next
        head = head.next
    return dummy.next
        
def MoveNthLastToFront(head,k):
    
    if not head or not head.next:
        return head
    
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    
    new_head = make_copy(head)
    prev = None
    curr = new_head
    count = length - k
    i = 0
    
    while curr and i < count:
        i += 1
        prev = curr 
        curr = curr.next 
        
    temp = curr
    prev.next = curr.next 
    temp.next = new_head
    return temp

def print_list(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.data, end=" -> ")
        else:
            print(curr.data)
        curr = curr.next
        
def main():
    print("Testing Happy Cases:")
    print("Original List")
    list1 = Node(15, Node(2, Node(8, Node(7, Node(20, Node(9, Node(11, Node(6, Node(19)))))))))
    print_list(list1) # 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
    print("Removing 2nd last node")
    list2 = MoveNthLastToFront(list1,2) # 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19
    print_list(list2)
    print("Removing 7th last node")
    list3 = MoveNthLastToFront(list1, 7) # 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
    print_list(list3)
    
    print()
    
    print("Testing edge cases:")
    list4 = Node(5) # 5
    list4 = MoveNthLastToFront(list4, 1)
    print_list(list4)
    list5 = Node(None) #none
    list5 = MoveNthLastToFront(list5, 0)
    print_list(list5)
    
if __name__ == "__main__":
    main()
