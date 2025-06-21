'''
Question 2: Build a Heap (40 min max)
Write a min heap class according to the following API using an array as the underlying data structure. (A max heap has the same implementation; you simply need to flip the direction of the comparators.) For simplicity, you can assume that the heap holds integers rather than generic comparables.

class Heap {
    private:
      array<int> arr; // the underlying array

    public:
      int top(); // returns the min (top) element in the heap
      void insert(int x); // adds int x to the heap in the appropriate position
      void remove(); // removes the min (top) element in the heap
}
'''

# arr to store the integers
# top()
#   return the arr[0] to return the min (top) element

# insert(int x)
#   append the x to the arr
#   increment our size
#   shift up the element to the appropriate position
#       - iterate until we reach index 0 and the curr element is less than its parent (we need parent index)
#           - swap it with the parent element
#           - update the curr index with parent index

# remove()
#   replace the first ele of arr with the last ele of arr
#   shift down the curr first ele to the appropriate position (we need children indices)
#       - check while the curr index is less than the size of arr
    #       - maintain min index which is curr index
    #       - check if the left child is less than the min index
    #           - update min index with left child index
    #       - check if the right child is less than the min index
    #           - update min index with right child index
    #       - check if the min index is not equal to curr index
    #           - swap the curr ele with the ele at min index
#       - call recursion func on the min index

class Heap: 
    arr = []
    
    # retrieving the smallest element in the heap
    def top(self):
        return self.arr[0] # return the min element in the arr
    
    # inserting the element in the heap
    def parent_index(self, i):
        return (i - 1) // 2
        
    def shift_up(self, i):
        # check if the curr index does not go out of bound and it is less than the parent index
        while i > 0 and self.arr[i] < self.arr[self.parent_index(i)]:
            # swap the curr ele with parent ele
            self.arr[i], self.arr[self.parent_index(i)] = self.arr[self.parent_index(i)], self.arr[i]
            # update the curr ele index
            i = self.parent_index(i)
            
    def insert(self, x):
        self.arr.append(x)
        self.shift_up(len(self.arr)-1)
    
    def left_child_index(self, i):
        return (i * 2) + 1
        
    def right_child_index(self, i):
        return (i * 2) + 2
        
    def shift_down(self, i):
        min_index = i # first, curr index is the smallest index

        # getting which child has the min index
        l_child_idx = self.left_child_index(i)
        if l_child_idx < len(self.arr) and self.arr[l_child_idx] < self.arr[min_index]:
            min_index = l_child_idx
            
        r_child_idx = self.right_child_index(i)
        if r_child_idx < len(self.arr) and self.arr[r_child_idx] < self.arr[min_index]:
            min_index = r_child_idx
       
        # swapping if the curr index is not equal to min index
        if i != min_index:
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            self.shift_down(min_index) # min index becomes the index of curr ele that was swapped
        
        
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
    arr_list.insert(5)
    arr_list.insert(9)
    arr_list.insert(2)
    arr_list.insert(3)
    arr_list.insert(1)
    arr_list.insert(6)
    print("Original Heap: ", end='')
    arr_list.print_heap()
    
    print('Testing remove function')
    arr_list.remove() # 2 5 9 3 6
    print('After removing the smallest element:', end='')
    arr_list.print_heap()
        
    print("Testing top function")
    smallest = arr_list.top()
    print(f"Smallest element: {smallest}")
    
if __name__ == '__main__':
    main()
     
# Time complexity - O(log n)
# Space complexity - O(n)
# Time taken - All code implemented in 40 mins, testing and debugging needs another 15-20 mins