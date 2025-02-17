'''

Question 4: BackspaceStringCompare
Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Examples:
Input Strings: "abcde", "abcde"
Output: True

Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
Output: True

Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True

Input Strings: "abcdef###xyz", "abcdefxyz###"
Output: False

'''

# first create maps for two strings
# get the freq of '#'
# iterate over the first str
#   check if the next ele is #
#       while the next eles are #
#           go back to prev elements and decrement the counts
# compare the two hashmaps

# dictionaries won't work because they didn't check orders.

# Two pointer with two arrays/strings approach
# two pointers; each pointing and iterating thru each str
# iterating until either of the str is exhausted
#   check if the l pointer pointing to the '#'
#       count the num of # and skip that amount of chars
#   check if the r pointer pointing to the '#'
#       count the num of # and skip that amount of chars
#   check if the l and r pointer elements are not the same
#       return false
                
def backspace_str_compare(s1, s2):
    
    l, r = len(s1) - 1, len(s2) - 1
    
    while l >= 0 and r >= 0:
            
        if s1[l] == '#':
            backspace_count = 0
            while s1[l] == '#':
                backspace_count += 1
                l -= 1
            l -= backspace_count
        
        if s2[r] == '#':
            backspace_count = 0
            while s2[r] == '#':
                backspace_count += 1
                r -= 1
            r -= backspace_count
            
        if s1[l] == s2[r]:
            l -= 1
            r -= 1
        else:
            return False
    
    # need to check if there are elements in each of the str
    while l >= 0:
        if s1[l] == '#':
            backspace_count = 0
            while s1[l] == '#':
                backspace_count += 1
                l -= 1
            l -= backspace_count
            
    while r >= 0:
        if s2[r] == '#':
            backspace_count = 0
            while s2[r] == '#':
                backspace_count += 1
                r -= 1
            r -= backspace_count
        
    if l == -1 and r == -1:
        return True
    else:
        return False
    
print(backspace_str_compare( "abcde", "abcde")) # true
print(backspace_str_compare("Uber Career Prep", "u#Uber Careee#r Prep")) # true
print(backspace_str_compare("abcdef###xyz", "abcw#xyz")) # true
print(backspace_str_compare("abcdef###xyz", "abcdefxyz###")) # false

# Time - O(m + n)
# Space - O(1)
# Time taken ~ 1hr