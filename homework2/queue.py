# Uber Career Prep 
# Homework 2
# Problem 4 - queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # returns the first item in the queue. O(1) time.
    def peek(self):
        return self.head.data
    
    # adds x to the back of the queue. O(1) time.
    def enqueue(self, data):
       new_node = Node(data)
       if self.isEmpty():
           self.head = new_node
           self.tail = new_node
           
       else:
           self.tail.next = new_node
           new_node.prev = self.tail
           self.tail = new_node
    
    # removes and returns the first item in the queue. O(1) time.
    def dequeue(self):
        first_node = self.head
        second_node = first_node.next
        self.head = second_node
        second_node.prev = None
        return first_node.data
    
    # returns a boolean indicating whether the queue is empty. O(1) time.
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
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.print_list() # 1->2
    
    print(q.isEmpty()) # False
    
    q.dequeue() 
    q.print_list() # 2
    
    q.enqueue(3) 
    q.print_list() # 2 -> 3
    q.peek() # 3
    
    q.dequeue()
    q.print_list() # 3

if __name__ == '__main__':
    main()