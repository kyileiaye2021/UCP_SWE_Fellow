# Uber Career Prep 
# Homework 2
# Problem 6 - deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # returns the first item in the deque. O(1) time.
    def front(self):
        return self.head.data
    
    # returns the last item in the deque. O(1) time.
    def back(self):
        return self.tail.data
    
    # adds x to the back of the deque. O(1) time.
    def pushBack(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def pushFront(self, x):
        new_node = Node(x)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    # removes and returns the first item in the deque. O(1) time.
    def popFront(self):
        if not self.head:
            return None
        
        removed_node = self.head
        second_node = self.head.next
        self.head = second_node
        second_node.prev = None
        return removed_node.data
    
    # removes and returns the last item in the deque. O(1) time.
    def popBack(self):
        if not self.head:
            return None
            
        removed_node = self.tail
        
        if self.head == self.tail: # only one node in the list
            self.head = self.tail = None
            
        else:
            second_to_last_node = self.tail.prev
            second_to_last_node.next = None
            self.tail = second_to_last_node
        return removed_node.data
        
    def isEmpty(self):
        return (not self.head and not self.tail)
    
    def print_list(self):
        curr = self.head
        while curr:
            if curr.next:
                print(curr.data, end=" -> ")
            else:
                print(curr.data)
            curr = curr.next
    
def main():
    q = Deque()
    q.pushBack(2)
    q.pushFront(1)
    q.print_list() # 1->2
    
    print(q.isEmpty()) # False
    
    print(q.front()) # 1
    print(q.back()) #2

    print(q.popBack()) # 2
    q.print_list() # 1
    

if __name__ == '__main__':
    main()