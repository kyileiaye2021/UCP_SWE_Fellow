'''
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, return the number of destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

Examples:
Input: [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

Origin = "New York", k=5
Output: 2 (["Boston", "Philadelphia"])

Origin = "New York", k=7
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

Origin = "New York", k=8
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])

'''

# graph algorithm (bfs)
# create a graph (undirected weighted)
# create a cities hashmap {'city': [('city', weight)]}
# return city graph

# create a city graph
# visited cities set
# weight = 0
# res list
# create a queue
# add the origin with weight to the queue  (origin, weight)
# until queue is empty
# for each neighbor in the city graph
#   check if the neighbor is not already visited
#   curr weight = weight + curr neighbor weight
#   if weight != 0
#       add 1 to curr weight
#   check if the curr weight is less than the given k
#       add the (curr neighbor, curr weight) to the queue
#       append the curr neighbor to res
from collections import defaultdict, deque

def city_graph(cities):
    city_map = defaultdict(list)
    
    for (sor, des, hr) in cities:
        city_map[sor].append((des, hr))
        city_map[des].append((sor, hr))
        
    return city_map
    
def vacation_des(cities, origin, k):
    city_map = city_graph(cities)
    visited_cities = set()
    res_lst = []
    
    queue = deque()
    queue.append((origin, 0))
    visited_cities.add(origin)
    
    while queue:
        curr_city, curr_hr = queue.popleft()
        for (neigbor_name, neighbor_hr) in city_map[curr_city]:
            if neigbor_name not in visited_cities:
                new_hr = curr_hr + neighbor_hr
                
                if curr_hr != 0:
                    new_hr += 1 # stopover
                    
                if new_hr <= k:
                    queue.append((neigbor_name, new_hr))
                    visited_cities.add(neigbor_name)
                    res_lst.append(neigbor_name)
    return res_lst

def main():
    input = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    origin = 'New York'
    k = 5
    print(vacation_des(input, origin, k)) # ['Boston', 'Philadelphia']
    
    origin = "New York"
    k=7
    print(vacation_des(input, origin, k)) # ["Boston", "Philadelphia", "Washington, D.C", "Newport"]
    
    origin = "New York"
    k=8
    print(vacation_des(input, origin, k)) # ["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"]
    
    origin = "New York"
    k = 2
    print(vacation_des(input, origin, k)) # ['Philadelphia']
    
    origin = "New York"
    k = 1
    print(vacation_des(input, origin, k)) # []
    
    
if __name__ == '__main__':
    main()
                    
# Time complexity - O(n + e)
# Space complexity - O(n + e)
# Time taken - ~45mins
    
