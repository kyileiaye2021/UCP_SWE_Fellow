
# def zerosum(lst):
#     freq = {}
#     counter = 0
#     for ele in lst:
#         if ele not in freq:
#             freq[ele] = 1
#         else:
#             freq[ele] += 1
    
#     for ele in lst:
#         if freq[ele] > 0:
#             freq[ele] -= 1
#             neg_val = 0 - ele
#             if neg_val in freq and freq[neg_val] > 0:
#                 freq[neg_val] -= 1
#                 counter += 1
                
#     return counter

# def main():
#     lst1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
#     print(zerosum(lst1)) # 2
    
#     lst2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
#     print(zerosum(lst2)) # 3
    
#     lst3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
#     print(zerosum(lst3)) # 0
    
#     lst4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
#     print(zerosum(lst4)) # 1
    
# main()