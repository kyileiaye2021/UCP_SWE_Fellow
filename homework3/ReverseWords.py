'''
Given a string, return the string with the order of the space-separated words reversed.

Examples:
Input: "Uber Career Prep"
Output: "Prep Career Uber"

Input: "Emma lives in Brooklyn, New York."
Output: "York. New Brooklyn, in lives Emma"

'''

# happy cases
# input: "Uber Career Prep"
# output: "Prep Career Uber"

# input: "Emma lives in Brooklyn, New York."
# output: "York. New Brooklyn, in lives Emma"

# edge cases
# input: "Emma"
# output: "Emma"

# input: "Joe Doe"
# output: "Doe Joe"

# input: ""
# output: ""

# two pointer technique? -> O(n+k) time?
# separating the str into a list of words? O(k) -> space ?
# separate the string into a list
# create l, r 
# iterate until l passes r
#   swap l and r ele
# combine the list words back into the str and return

def reverse_words(str):
    words = str.split(' ')
    l, r = 0, len(words)-1
    
    while l < r:
        words[l], words[r] = words[r], words[l]
        l += 1
        r -= 1
        
    return ' '.join(words)

def main():
    str1 = "Uber Career Prep"
    print(reverse_words(str1)) # "Prep Career Uber"
    
    str2 = "Emma lives in Brooklyn, New York."
    print(reverse_words(str2)) # "York. New Brooklyn, in lives Emma"
    
    str3 = "Emma"
    print(reverse_words(str3)) # "Emma"

    str4 = "Joe Doe"
    print(reverse_words(str4)) # "Doe Joe"
    
    str5 = ""
    print(reverse_words(str5)) # ""
    
if __name__ == '__main__':
    main()
    
# time complexity - O(k) k words in the str
# space complexity - O(k) k words in the list
# Time taken - ~10mins