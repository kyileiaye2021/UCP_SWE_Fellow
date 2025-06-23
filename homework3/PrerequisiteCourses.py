'''
Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, return a valid order for them to take their courses assuming they only take one course for their major at once.

Examples:
Input: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
Output: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"] or 
["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]

Input: ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
Output: ["Intro to Writing", "Plays & Screenplays", "Contemporary Literature", "Ancient Literature", "Comparative Literature"] or
["Intro to Writing", "Contemporary Literature", "Plays & Screenplays", "Ancient Literature", "Comparative Literature"] or
["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Plays & Screenplays", "Comparative Literature"] or 
["Intro to Writing", "Ancient Literature", "Contemporary Literature",  "Plays & Screenplays", "Comparative Literature"] or 
["Intro to Writing", "Ancient Literature",  "Plays & Screenplays",  "Contemporary Literature", "Comparative Literature"] or
["Intro to Writing", "Plays & Screenplays", "Ancient Literature",  "Contemporary Literature", "Comparative Literature"] or 
["Intro to Writing", "Ancient Literature",  "Contemporary Literature", "Comparative Literature", "Plays & Screenplays"] or 
["Intro to Writing", "Contemporary Literature",  "Ancient Literature", "Comparative Literature", "Plays & Screenplays"] 
'''

# topological sort (bfs)
# create a graph 
# graph map {preq course : [next courses]}
# iterate thru given hashmap 
#   iteraet thru each val
#       adding the curr key to the graph map

# create a indeg hashmap {'course name': num of indeg }
# create a graph by calling the above func
# iterate thru preq course in the graph map 
#   iterate thru the next courses
#       increment indeg of each course name
# create a queue
# add the courses with no indeg to the queue
# until the queue is empty
#   pop out the ele 
#   iterate thru each next coures of the curr preq course
#       decrement their indeg values in indeg map
#       check if the indeg value of the curr next course is 0
#           add it to the queue

from collections import defaultdict, deque

def preq_courses_graph(course_map):
    
    course_connection = defaultdict(list)
    
    for next_course in course_map:
        
        for preq_courses in course_map[next_course]:
            
            course_connection[preq_courses].append(next_course)
            
    return course_connection
    
def prequisite_courses(course_lst, course_map):
    res_course_lst = []
    course_graph = preq_courses_graph(course_map) # {preq : [post]}
    taken_course = set()
    
    preq = {course: 0 for course in course_lst} # {course name : preq num}
    
    for course in course_graph:
        for postrequisite in course_graph[course]:
            preq[postrequisite] += 1
            
    queue = deque()
    # add the courses with no preq to the queue
    for course in preq:
        if preq[course] == 0:
            queue.append(course)
            taken_course.add(course)
            
    while queue:
        curr_course = queue.popleft()
        res_course_lst.append(curr_course)
        
        for postrequisite in course_graph[curr_course]:
            preq[postrequisite] -= 1
            if preq[postrequisite] == 0:
                queue.append(postrequisite)
                taken_course.add(postrequisite)
    return res_course_lst

def main():
    
    input = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    courses = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
    print(prequisite_courses(input, courses)) # ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]
    print()
    input = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    courses = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    print(prequisite_courses(input, courses))
    print()
    input = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    courses = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Contemporary Literature"]}
    print(prequisite_courses(input, courses)) # ['Intro to Writing', 'Comparative Literature', 'Plays & Screenplays', 'Contemporary Literature', 'Ancient Literature']
    print()
               
if __name__ == '__main__':
    main()