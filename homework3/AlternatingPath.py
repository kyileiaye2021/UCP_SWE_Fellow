'''
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.

Examples:
[(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"), (C, B, "red"), (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]

Input: origin = A, destination = E
Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

Input: origin = E, destination = D
Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))

'''

# TRIED THIS APPROACH WITHIN THE 40mins TIME
# Directed Weighted Graph with dfs

# dfs func
# make the curr node as visited
# have curr node's color
# if weight color is not none and curr node's color is the same as the passed arg weight color
#   return
# else : increment our path count
# for each neighbor
#   check if the curr neighbor is not visited
#       call recursive func on the neighbor (curr neighbor, curr node's weight color)
# 
# connect the nodes with the color weight
# visited set
# iterate thru the list
#   check if the curr node is not visited
#       call dfs on the curr node

# bfs # I need to look at some references for this problem
from collections import defaultdict, deque

def create_graph(connections):
    graph_map = defaultdict(list)
    
    for (org, des, color) in connections:
        graph_map[org].append((des, color))
        
    return graph_map
        
def alternating_path(connections, org, des):
   graph = create_graph(connections)
   visited = set()
   queue = deque()
   
   queue.append((org, None, 0))
   visited.add((org, None))
   
   path_len = 0
   while queue:
       # pop out the curr node
       curr_node, curr_color, path_len = queue.pop()
       
       if curr_node == des:
           return path_len
       
       # check out the neighbor
       for (neighbor, neighbor_color) in graph[curr_node]:
           
           if (neighbor, neighbor_color) not in visited:
               # check if the colors are alternating
               if neighbor_color != curr_color:
                   queue.append((neighbor, neighbor_color, path_len + 1))
                   visited.add((neighbor, neighbor_color))
    
       
   return -1
     
def main():
    input = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]
    origin = 'A'
    destination = 'E'
    output = alternating_path(input, origin, destination)
    print(output) # 4
    
    origin = 'D'
    destination = 'B'
    output = alternating_path(input, origin, destination)
    print(output) # 2
    
    origin = 'E'
    destination = 'D'
    output = alternating_path(input, origin, destination)
    print(output) # -1

if __name__ == '__main__':
    main()
    
# Time complexity - O(v + e)
# Space complexity - O(v + e)
# Time taken - more than 1 hours