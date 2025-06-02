"""Question 1: Graph Algorithms Using Adjacency List/Set Representation (1 hr, 40 min max)
Given an array of pairs of values representing edges in an unweighted graph, create the equivalent adjacency list/set representation (a map from element to a list or set of elements). 
Pairs represent directed edges: (A, B) means there is an edge from A to B. If the pair (B, A) is also provided, then there is an undirected edge between A and B. 
For simplicity, you may assume that each node of the graph stores an integer rather than a generic data type and that the elements are distinct. 
Implement a basic DFS and BFS that search for a target value and two topological sorts (using each of DFS and Kahn’s algorithm).

// Build graph representation. You can also use an array rather than a set
map<int, set<int>> adjacencySet(array<pair<int, int>> edges);

// Example
Input: [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
Output:
{
    0: []
    1: [2, 3]
    2: [0, 3]
    3: [2]
}

bool bfs(int target, map<int, set<int>> graph);
bool dfs(int target, map<int, set<int>> graph);
array<int> topologicalSort(map<int, set<int>> graph);
array<int> topologicalSortDfs(map<int, set<int>> graph);

"""

# FIND THE TARGET WITH BFS AND DFS
# create a graph func 
# create the adj list - 2d list
# create a list for each index in the vertex list 
# iterate thru the edges
#   first value of each pair = curr vertex list
#   add the second value of each pair to the curr vertex list
# return the graph

# bfs helper func
# para = queue, visited, i, target
# add the vertex i to the queue and mark it as visited
# until the queue is empty
#   pop the front of the queue
#   check if the curr vertex is equal to target
#       return True
#   for each neighbor in the curr vertex list
#       check if the neighbor is not visited 
#           add the neighbor in the queue
# return False

# bfs func
# for bfs, visited, i, v, edges, target value as parameters
# create a graph
# iterate thru each vertex in the graph
#   check if the vertex is not visited 
#       bfs helper on that vertex and store it in res
# return res

# dfs helper func
# parameter would be visited, i, target, found (bool)
# mark the current vertex as visited
# check if the current vertex is == target
#   return true
# for each neighbor in the curr vertex list
#   call recursive func on the neighbor
# return False

# dfs func
# create a graph
# iterate thru each vertex in the graph
#   check if the vertex is not visited 
#       dfs helper on that vertex and store it in res
# return res

# TOPOLOGY SORT WITH BFS AND DFS    
# bfs_topology
# calculate indegree of each vertex
# create indegree list with the size of vertex all initialized to 0 first
# add the vertex with indegree 0 to queue
# add the vertex in the res list
# until queue is empty
#   pop out the front of the queue
#   add the curr vertex to the res list
#   for each neighbor in the curr vertex list
#       decrement the indegree of neighbor
#       check if the neighbor has 0 indegree
#           add the neighbor to the queue
# return res list

# dfs_topology helper func
# parameter would be visited, i, target, stack
# mark the current vertex as visited
# for each neighbor in the curr vertex list
#   call recursive func on the neighbor
# add the curr vertex to the stack 
# return the stack

# dfs_topology 
# create a graph
# iterate thru each vertex in the graph
#   check if the vertex is not visited 
#       dfs_topology helper on that vertex and store it in res
# return res

# TIME COMPLEXITY - O(V + E)
# SPACE COMPLEXITY - O(V)
# Time taken - ~1hr

from collections import deque

def create_graph(v, edges, is_topological):
    adj = [[] for _ in range(v)]
    
    for i, j in edges:
        adj[i].append(j)
        if not is_topological:
            adj[j].append(i)
    return adj
  
def bfs_helper(visited, i, adj, target):
    queue = deque()  
    queue.append(i)
    visited[i] = True
    
    while queue:
        curr = queue.popleft()
        if curr == target:
            return True
        
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                
    return False
    
def bfs(v, edges, target):
    adj = create_graph(v, edges, False)
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            if bfs_helper(visited, i, adj, target):
                return True
            else:
                return False
         
def dfs_helper(visited, i, adj, target, found):
    visited[i] = True
    if target == i:
        found[0] = True
    
    for neighbor in adj[i]:
        if not visited[neighbor]:
            dfs_helper(visited, neighbor, adj, target, found)
    return found

def dfs(v, edges, target):
    found = [False]
    adj = create_graph(v, edges, False)
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            dfs_helper(visited, i, adj, target, found)
            if found[0]:
                return True
            else:
                return False              

def bfs_topology(v, edges):
    adj = create_graph(v, edges, True)
    indegree = [0] * v 
    res = []
    
    for i, j in edges:
        indegree[j] += 1
        
    queue = deque()
    for i in range(v):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        curr = queue.popleft()
        res.append(curr)
        
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)      
        
    return res
    
def dfs_topology_helper(v, adj, visited, stack):
    visited[v] = True
    
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs_topology_helper(neighbor, adj, visited, stack)
    
    stack.append(v)

def dfs_topology(v, edges):
    stack = []
    adj = create_graph(v, edges, True)
    visited = [False] * v
    for i in range(v):
        if not visited[i]:
            dfs_topology_helper(i, adj, visited, stack)
    return stack[::-1]
        
input = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
v = len(input)

# case1: the target is in the graph
print("#######Checking the target which is in the graph######")
target = 1
print(f"1 is in the graph(BFS)?: {bfs(v,input, target)}")
print(f"1 is in the graph(DFS)?: {dfs(v,input, target)}")

# case2: the target is not in the graph
print("#######Checking the target which is not in the graph######")
target = 5
print(f"5 is in the graph(BFS)?: {bfs(v,input, target)}")
print(f"5 is in the graph(DFS)?: {dfs(v,input, target)}")

# topological sort 
# bfs
input2 = [(1, 3), (1,2), (0,1), (2,4)]
v2 = 5
print(f"BFS Topological Sort: {bfs_topology(v2, input2)}")
# dfs
print(f"DFS Topological Sort: {dfs_topology(v2, input2)}")


