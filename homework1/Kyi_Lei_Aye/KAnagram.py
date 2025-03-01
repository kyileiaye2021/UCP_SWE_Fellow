'''Question 7: KAnagrams
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Examples:
Input Strings: "apple", "peach"
Input k: 1
Output: False

Input Strings: "apple", "peach"
Input k: 2
Output: True

Input Strings: "cat", "dog"
Input k: 3
Output: True

Input Strings: "debit curd", "bad credit"
Input k: 1
Output: True

Input Strings: "baseball", "basketball"
Input k: 2
Output: False

'''

# happy case
# input: "ab", "abd", k = 1
# output: True

# input: "ab", "ac", k = 1
# output: True

# input: "a", "ab", k = 1
# output : True

# Edge cases
# input: "cab", "db", k = 2
# output: True

# can be hash sth problem
# use hashmap to count the chars

# create a hashmap for one str
# iterate over the another str
#   check if the curr char is in the hashmap
#       check if curr char count in hashmap is greater than 0
#           decrement that count of hashmap by 1
#   if not in hashmap, 
#       check if k is not greater than 0
#           return false
#       else: decrement k by 1

# iterate over the hashmap and check the count of the the values in hashmap
# if the count of value is not equal to k 
#   return false
# return true

from collections import Counter

def kAnagram(s1, s2, k):
    s2_hashmap = {}
    temp = 0
    
    for ele in s2:
        s2_hashmap[ele] = s2_hashmap.get(ele, 0) + 1
        
    for ele in s1:
        if ele in s2_hashmap and s2_hashmap[ele] > 0:    
            s2_hashmap[ele] -= 1
                
        else:
            if temp > k:
                return False
            else:
                temp += 1
    
    counter = 0        
    for count_value in s2_hashmap.values():
        counter += count_value
    
    if temp != k and counter != k:
        return False
    
    return True

s1 = "apple"
s2 = "peach"
k = 1
print(kAnagram(s1,s2,k)) #False

s1 = "apple"
s2 = "peach"
k = 2
print(kAnagram(s1,s2,k)) #True

s1 = "cat"
s2 = "dog"
k = 3
print(kAnagram(s1,s2,k)) #True

s1 = "debit curd"
s2 = "bad credit"
k = 1
print(kAnagram(s1,s2,k)) #True

s1 = "baseball"
s2 = "basketball"
k = 2
print(kAnagram(s1, s2,k)) #False

# Time complexity - O(n)
# Space complexity - O(m)
# Time ~20mins + 10mins debugging
'''
Note: I don't know why the last test case doesn't pass. but, I just realized that I can check the size of the two strings
if they are equal or not.
'''

'''-------------------------------------------------------------'''
# I tried another way using two dictionaries
from collections import Counter

def alternative_kAnagram(s1, s2, k):
    if len(s1) != len(s2):
        return False
    s1_dict = Counter(s1)
    s2_dict = Counter (s2)
    count = 0
    
    for ele in s1_dict:
        if ele in s2_dict:
            count += abs(s1_dict[ele] - s2_dict[ele])
        else:
            count += 1
            
    if count > k:
        return False
    return True

s1 = "apple"
s2 = "peach"
k = 1
print(alternative_kAnagram(s1,s2,k)) #False

s1 = "apple"
s2 = "peach"
k = 2
print(alternative_kAnagram(s1,s2,k)) #True

s1 = "cat"
s2 = "dog"
k = 3
print(alternative_kAnagram(s1,s2,k)) #True

s1 = "debit curd"
s2 = "bad credit"
k = 1
print(alternative_kAnagram(s1,s2,k)) #True

s1 = "baseball"
s2 = "basketball"
k = 2
print(alternative_kAnagram(s1, s2,k)) #False

# Time complexity - O(n)
# Space complexity - O(m)
# Time ~30mins