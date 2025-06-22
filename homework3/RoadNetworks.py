'''
In some states, it is not possible to drive between any two towns because they are not connected to the same road network. Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. (For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the towns are connected by roads has 0 road networks.)

Examples:
Input: ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]

Output: 2 (Networks are Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)

Input: ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]

Output: 3 (Networks are Kona-Hilo-Volcano, Haiku-Kahului-Lahaina-Hana, and Lihue-Waimea-Princeville)

Edge case
if there is no connected town -> 0
'''
# graph algorithm
# bfs helper
# mark the curr town as visited - put the curr town name. into the set\
# create a str
# create a queue
# add the curr town list into the queue
# until queue is empty
#   pop out the curr town from the queue
#   concat the curr town to the str
#   check the neighbors of the curr town 
#   check that they are in the hashmap and not visited
#       add them to the queue
#       add the names to the set
# return the str
#   
# connect the two towns first
# create a hashmap {'': []}
# create a set
# iterate thru the tuples
#   adding the key val pairs into the map
#   add the key in the val as val as well # undirected graph
# create res str: 'Networks are '
# iterate thru the hashmap
#   check if the curr town is not visited
#       curr str = call bfs on the curr town
#       concat the curr str to the res str ,

from collections import deque, defaultdict

def bfs(town, town_map, visited_towns):
    visited_towns.add(town)
    queue = deque()
    queue.append(town)
    
    while queue:
        curr_town = queue.pop()
        for neighbor in town_map[curr_town]:
            if neighbor not in visited_towns:
                queue.append(neighbor)
                visited_towns.add(neighbor)
                
    
def connect_towns(connections):
    town_map = defaultdict(list)
    for (sour, des) in connections:
        town_map[sour].append(des)
        town_map[des].append(sour)
    return town_map
    
def road_network(towns, connections):
    # creating a graph
    town_map = connect_towns(connections)
    # keep track of visited towns
    visited_towns = set()
    
    connected_town_count = 0
    
    for town in town_map:
        
        if town not in visited_towns:
            bfs(town, town_map, visited_towns)
            connected_town_count += 1
            
    return connected_town_count
    
def main():
    
    towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
    connections = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    
    res = road_network(towns, connections) # (Networks are Gustavus-Glacier Bay and Anchorage-Fairbanks-McCarthy-Copper Center-Homer-Healy)
    print(res) # 2 
    
    towns1 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    connections1 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    res1 = road_network(towns1, connections1)
    print(res1) # 3

    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    connections2 = []
    res2 = road_network(towns2, connections2)
    print(res2)  # 0

if __name__ == '__main__':
    main()
    
# Time complexity - O(n) if in the worst case, every town is connected to each other
# Space complexity - O(n) 
# time taken - ~1 hr
# I finished brainstorming and most part of coding within first 40mins, and spend the rest debugging and adding some part of the code