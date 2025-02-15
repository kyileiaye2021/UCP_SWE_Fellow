# Question 2: ReverseVowels
# Given a string, reverse the order of the vowels in the string.

# Examples:
# Input String: "Uber Career Prep"
# Modified String: "eber Ceraer PrUp"

# Input String: "xyz"
# Modified String: "xyz"

# Input String: "flamingo"
# Modified String: "flominga"

# happy cases
# input str: "Uber Career Prep"
# output: "eber Ceraer PrUp"

# input str: "abe"
# output: "eba"

# Edge cases
# input str: "ab"
# output: "ab"

# input str: "a"
# output: "a"

# input str: "xyz"
# output: "xyz"

# FOrward backward two pointer approach
# create a set for storing vowels
# create two pointers; one pointing to the first and the other pointint last in the str
# iterate thru the str until left pointer passes right pointer
#   check if both pointer elements are the same
#       swap two ele and shift the pointers
#   check if left pointer element is a vowel and right is not
#       decrement right by 1
#   check if right pointer element is a vowel and left is not
#       increment left by 1
#   otherwise: shift both element
# return str

def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o','u'}
    s = list(s)
    l, r = 0, len(s) - 1
    
    while l < r:
        if s[l].lower() in vowels and s[r].lower() in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        elif s[l].lower() in vowels and s[r].lower() not in vowels:
            r -= 1
        
        elif s[l].lower() not in vowels and s[r].lower() in vowels:
            l += 1
            
        else:
            l += 1
            r -= 1
    s = ''.join(s)       
    return s

input = "Uber Career Prep"
print(reverse_vowels(input)) # "eber Ceraer PrUp"

input = "xyz"
print(reverse_vowels(input)) #"xyz"

input = "flamingo"
print(reverse_vowels(input))# "flominga"

# Time complexity - O(n)
# Space complexity - O(n)
# Time taken ~ 15 mins