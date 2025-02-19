'''
Question 5: ShortestSubstring
Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.

Examples:
Input Strings: "abracadabra", "abc"
Output: 4
(Shortest Substring: "brac")

Input Strings: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
Output: 10
(Shortest Substring: "zzxwdcbxyz")

Input Strings: "dog", "god"
Output: 3
(Shortest Substring: "dog")

'''

# Happy case
# input: s1 = 'abcbde' , s2 = 'abd'
# output: 5 (abcbd)

# input: s1 = 'abc', s2 = 'bcd'
# output: 2 (bc)

# Edge case
# input: s1 = 'a', s2 = 'ab'
# output: 1 

# input: s1 = 'ab', s2 = 'a'
# output: 'a'

# brute force approach with nested loop - O(n^2):iterating thru the list and check if the chars starting from the curr char are in s2 and keep track of the smallest substr
# sliding window with variable size - O(n)

# we can use a dict as we don't need the order of s2 but require the freq of s2 chars

# l and r
# shortest_substr_count = 0
# curr_substr_count = 0
# formed = 0
# curr_window_dict = {}
# create a dict to store the str2's chars and their frequencies
# while r is less than the len of the str1
#   add the curr char to curr_window_dict
#   if curr char in s2 dict and if freq of curr char in curr window is equal to the freq of that char in s2 dict
#       increment formed by 1
#   increment curr_substr_count by 1
#   increment r pointer by 1
#   update the shortest_substr_count
#   while formed is equal to the len of the str2 dict
#       update the freq of curr window dict
#       if the l ele is in s2 and if l ele freq in curr window is less than the freq in s2 dict:
#           decrement formed by 1
#       move l pointer by 1
# return shortest substr len

def shortest_substr(s1, s2):
    l, r = 0, 0
    shortest_substr_count = float('inf')
    valid = 0 # to check that the current window contains all required elements in s2
    
    s2_dict = {}
    for ele in s2:
        s2_dict[ele] = s2_dict.get(ele, 0) + 1
    
    curr_window_dict = {} # to keep track of each current window
    
    while r < len(s1):
        # expanding the curr window until the curr window covers every element in s2
        curr_window_dict[s1[r]] = curr_window_dict.get(s1[r], 0) + 1 # populating the curr window dict with the curr val
        if s1[r] in s2 and curr_window_dict[s1[r]] == s2_dict[s1[r]]:
            valid += 1
        
        r += 1
        
        # shrinking the curr window
        while valid == len(s2_dict):
            shortest_substr_count = min(shortest_substr_count, (r - l))

            # here we have to make sure that all required elements in the s2 are in the current window so need to check before moving the l pointer 
            if s1[l] in s2_dict and curr_window_dict[s1[l]] == s2_dict[s1[l]]: # if the left pointer points to required char 
                valid -= 1
                
            curr_window_dict[s1[l]] -= 1 # decrement the freq of the l pointer char 
                
            l += 1
            
    return shortest_substr_count

s1 = "abracadabra"
s2 = "abc"
print(shortest_substr(s1, s2)) # 4
# (Shortest Substring: "brac")

s1 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
s2 = "zzyzx" 
print(shortest_substr(s1, s2)) #10
# (Shortest Substring: "zzxwdcbxyz")

s1 = "dog"
s2 = "god"
print(shortest_substr(s1,s2)) #3
# (Shortest Substring: "dog")

# Time complexity - O(n + k)
# Space complexity - O(m + k)
# time taken - more than 1 hour