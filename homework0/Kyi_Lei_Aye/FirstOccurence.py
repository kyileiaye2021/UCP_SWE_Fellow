# Given a string, return a string that contains only the first occurrence of each character in the string.

# Examples:
# Input String: "abracadabra"
# Output: "abrcd"

# Input String: "Uber Career Prep"
# Output: "Uber CaPp"

# Input String: "zzyzx"
# Output: "zyx"

# Set container appraoch
# set is unordered so i used list instead
# initialize the list container
# iterate over the input string
#    check if the curr char is not in the set
#       add the curr ele in the set
# join the chars of the set and assign it to a new str
# return the new str

# Time complexity - O(n)
# Space complexity - O(n)
def first_occurence(list):
    unique = []

    for ele in list:
        if ele not in unique:
            unique.append(ele)

    res = ''.join(unique)
    return res

def main():
    str1 = "abracadabra"
    print(first_occurence(str1)) # "abrcd"
    
    str2 = "Uber Career Prep"
    print(first_occurence(str2)) # "Uber CaPp"
    
    str3 = "zzyzx"
    print(first_occurence(str3)) # "zyx"
    
main()

# Time spent - ~10min