# Uber Career Prep 
# Homework 2
# Problem 5 - stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Stack:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    # returns the top item in the stack. O(1) time.
    def top(self):
        return self.tail.data
    
    # adds x to the top of the stack. O(1) time.
    def push(self, data):
        
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    # removes and returns the top item in the stack. O(1) time.
    def pop(self):
        if not self.head:
            return None
        
        removed_node = self.tail
        if self.head == self.tail:
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
    
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.print_list() # 10 -> 20
   
    print(stack.isEmpty())# False
    
    print(stack.pop()) # 20
    stack.print_list() #10

if __name__ == "__main__":
    main()