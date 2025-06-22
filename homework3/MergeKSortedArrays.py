'''
Question 9: MergeKSortedArrays
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

Examples:
Input: 2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

Input: 3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
'''

# happy cases
# input: 2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
# output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

# edge cases
# input: 0, []
# output: []

# input: 1, [[1,4,6,7]]
# output: [1,4,6,7]

# Using pointers and moving them simultaneously -> time- O(k * n) since we have to iterate thru every n element in each list
# Using min heap -> can be more efficient in time complexity

# create min heap
# create res list
# iterate thru each array
# add the (val, array index, ele index) to the min heap
# until min heap is empty
# pop the ele from the left (val, array index, ele index)
# append the val to the res list
# go to next index of curr list (array index)
# check if the next ele index doesn't exceed the len of curr list
#   add the next ele to the res
#   add the () to the min heap
import heapq
def MergeKSortedArray(k, arrays):
    res_lst = []
    min_heap = []
    
    # add the first elements of each arr into the min heap
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(min_heap, (arrays[i][0], i, 0))
    
    # pop out the smallest ele and add the next ele into the min heap    
    while min_heap:
            
        # pop out the smallest pair
        val, arr_index, ele_index = heapq.heappop(min_heap)
        res_lst.append(val)
            
        if ele_index + 1 < len(arrays[arr_index]):# adding new ele of the curr list
            heapq.heappush(min_heap, (arrays[arr_index][ele_index + 1], arr_index, ele_index+1))
                
    return res_lst

def main():
    
     k = 2 
     arrays = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
     print(MergeKSortedArray(k, arrays)) # [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
     
     k = 3
     arrays = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
     print(MergeKSortedArray(k, arrays)) # [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
     
     k = 0
     arrays = []
     print(MergeKSortedArray(k, arrays)) # []
     
     k = 1
     arrays = [[1,3,6,7]]
     print(MergeKSortedArray(k, arrays)) # [1,3,6,7]
      
    
if __name__ == '__main__':
    main()
                
# Time complexity - O(nlogk) as heappush and heappop takes log n and we are doing it n times since there are n elements in subarrays
# space complexity - O(k)
# time taken - more than 1hr
        
        

