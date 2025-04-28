# Given a singly linked list, disconnect the cycle, if one exists.

# Happy cases:
# input: 10->18->12->9->11->4
                # |_________|
# output: 10->18->12->9->11->4

# input: 10->18->12->9->11->4_
#                           |_|
# output: 10->18->12->9->11->4

# Edge cases
# input: None
# output: None

# input: 1
# output: 1

# input: 1->4->3
# output: 1->4->3

# fast slow pointer

# if the list is empty, return none
# set fast and slow pointers to head
# set prev to none
# initialize cycle_found to false
# while fast is not none
#   check if the fast and slow pointers meet
#      update cycle_found status
#      break
#   move slow pointer by 1 node at a time
#   update prev to fast pointer
#   move fast pointer by 2 node at a time
# check if the cycle_found is false:
#   return head
# set the slow pointer to head again
# until the fast and slow pointers meet again
#   move slow by 1 node at a time
#   update prev to fast
#   move fast by 1 node at a time
# set prev.next to none
# return head
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def DisconnectCycle(head):
    if not head:
        return None
    
    fast, slow = head, head
    prev = Node(0)
    cycle_found = False
            
    while fast and fast.next:
        slow = slow.next 
        prev = fast
        fast = fast.next.next 
        
        if slow == fast:
            cycle_found = True
            break
            
    
    if not cycle_found:
        return head
    
    slow = head
    while slow != fast:
        slow = slow.next 
        prev = fast
        fast = fast.next
        
    prev.next = None
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
    
    # Testing lists that have cycles
    node1 = Node(10)
    node2 = Node(18)
    node3 = Node(12)
    node4 = Node(9)
    node5 = Node(11)
    node6 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    list1 = node1
    list1 = DisconnectCycle(list1)
    print_list(list1)
    
    node6.next = node6
    list2 = node1
    list2 = DisconnectCycle(list2)
    print_list(list2)
    
    list3 = Node(2)
    list3.next = list3
    list3 = DisconnectCycle(list3)
    print_list(list3)
    
    list4 = None
    list4 = DisconnectCycle(list4)
    print(list4)

if __name__ == '__main__':
    main()
    
# Time complexity - O(n)
# Space complexity - O(1)
# Time - ~30 mins