'''
Question 3: Build a Priority Queue (20 min max)
A priority queue functions like a queue except that elements are removed in order of priority rather than insertion. This is typically implemented as a max heap that stores pairs of elements and numeric weights, with the weights used as the values in the heap. Implement a priority queue according to the following API using a heap as the underlying data structure. For simplicity, you can assume the priority queue stores string elements with integer priorities. Start by copy-pasting your heap implementation from question 2 and making modifications.

class PriorityQueue {
    private:
      array<pair<string, int>> arr; // the underlying array

    public:
      int top(); // returns the highest priority (first) element in the PQ
      void insert(string x, int weight); // adds string x to the PQ with priority weight
      void remove(); // removes the highest priority (first) element in the PQ
}

'''

class Heap: 
    arr = [] # need to store tuples in the list
    
    # retrieving the smallest element in the heap
    def top(self):
        if not self.arr:
            return -1
        return self.arr[0] # return the min element in the arr
    
    # inserting the element in the heap
    def parent_index(self, i):
        return (i - 1) // 2
        
    def shift_up(self, i, w):
        # check if the curr index does not go out of bound and it is greater than the parent index
        while i > 0 and w > self.arr[self.parent_index(i)][1]:
            # swap the curr ele with parent ele
            self.arr[i], self.arr[self.parent_index(i)] = self.arr[self.parent_index(i)], self.arr[i]
            # update the curr ele index
            i = self.parent_index(i)
            
    def insert(self, x, w):
        self.arr.append((x, w))
        self.shift_up(len(self.arr)-1, w)
    
    def left_child_index(self, i):
        return (i * 2) + 1
        
    def right_child_index(self, i):
        return (i * 2) + 2
        
    def shift_down(self, i):
        max_index = i # first, curr index is the smallest index

        # getting which child has the min index
        l_child_idx = self.left_child_index(i)
        if l_child_idx < len(self.arr) and self.arr[l_child_idx][1] > self.arr[max_index][1]: # we have to compare weights
            max_index = l_child_idx
            
        r_child_idx = self.right_child_index(i)
        if r_child_idx < len(self.arr) and self.arr[r_child_idx][1] > self.arr[max_index][1]:
            max_index = r_child_idx
       
        # swapping if the curr index is not equal to min index
        if i != max_index:
            self.arr[i], self.arr[max_index] = self.arr[max_index], self.arr[i]
            self.shift_down(max_index) # min index becomes the index of curr ele that was swapped
        
        
    def remove(self):
        # replace the first ele with last ele in the array
        self.arr[0] = self.arr[-1]
        
        # remove the last ele
        self.arr = self.arr[:-1]
        
        self.shift_down(0)
    
    def print_heap(self):
        i = 0
        while i < len(self.arr): # 1 2 5 9 3 6
            print(self.arr[i], end=' ') 
            i += 1
        print('\n')
        
def main():
    arr_list = Heap()
    
    # Testing insert function 
    print("Testing insert function")
    arr_list.insert('a', 2)
    arr_list.insert('b', 5)
    arr_list.insert('c', 3)
    arr_list.insert('d', 1)
    arr_list.insert('e', 0)
    arr_list.insert('f', 6)
    print("Original Queue: ", end='')
    arr_list.print_heap() # f a b d e c
    
    print('Testing remove function')
    arr_list.remove() # b a c d e
    print('After removing the smallest element:', end='')
    arr_list.print_heap()
        
    print("Testing top function")
    smallest = arr_list.top()
    print(f"Smallest element: {smallest}")
    
if __name__ == '__main__':
    main()
     
# Time complexity - O(log n)
# Space complexity - O(n)
# Time taken - 25 mins 
# I learned that we have to compare weights instead of values in the array