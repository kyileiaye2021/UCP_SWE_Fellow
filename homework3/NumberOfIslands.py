'''
Given a binary matrix in which 1s represent land and 0s represent water, return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
'''

# happy cases
# input: [1 0 1 1 1
#         1 1 0 1 1 
#         0 1 0 0 0
#         0 0 0 1 0
#         0 0 0 0 0]
# output: 3

# input: [1 0 0 0 0
#         0 1 0 0 0 
#         0 0 1 0 0
#         0 0 0 1 0
#         0 0 0 0 1]
# output: 5

# input: [1 1 1 1
#         0 0 0 0]
# output: 1

# edge cases
# input: [0 0 0]
# output: 0

# input: [1 0 0
#         0 0 0]
# output: 1

# input: None
# output: 0

# DFS for this graph problem
# dfs func
# mark the curr cell as visited
# 4 directions we can go from the curr cell: left, right, bottom, and above
# iterate thru the 4 directions
#   find the new row and col
#   check if the curr cell is within the range of matrix and is 1
#       call dfs on it 

# initialize count to 0
# dimension: num of rows and columns
# iterate thru the rows
#   itrate thru the cols
#       check if the curr cell is 1
#           call dfs on that cell
#           increment count

def dfs(matrix, r, c):
    matrix[r][c] = 0
    directions = [[-1,0], [1,0], [0,1], [0,-1]]
    
    for dir_r, dir_c in directions:
        new_r = dir_r + r
        new_c = dir_c + c
        if new_r in range(len(matrix)) and new_c in range(len(matrix[0])) and matrix[new_r][new_c] == 1:
            dfs(matrix, new_r, new_c)
        
def numOfIslands(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dfs(matrix, r, c)
                count += 1
                
    return count

def main():
    
    matrix1 = [[1,0,1,1,1],
               [1,1,0,0,0],
               [0,1,0,1,0],
               [0,0,0,0,0]]
    print(numOfIslands(matrix1)) # 3
    
    matrix2 = [[1,0,0,0,0],
               [0,1,0,0,0],
               [0,0,1,0,0],
               [0,0,0,1,0]]
    print(numOfIslands(matrix2)) # 4
    
    matrix3 = [[1,0,0],
              [0,0,0]]
    print(numOfIslands(matrix3)) # 1
    
    matrix4 = [[0,0,0]]
    print(numOfIslands(matrix4)) # 0
    
    matrix5 = None
    print(numOfIslands(matrix1)) # 0
    
main()
# Time - O(m * n)
# Space - O(1)
# Time taken - ~20mins