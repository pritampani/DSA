# from collections import defaultdict
# class Solution:

#     def anagrams(self, arr):
#         '''
#         words: list of word
#         n:      no of words
#         return : list of group of anagram {list will be sorted in driver code (not word in grp)}
#         '''

#         #code here
#         res=defaultdict(list)
#         print(res)
#         for s in arr:
#             count=[0]*26
#             for c in s:
#                 count[ord(c)-ord("a")]+=1
#             res[tuple(count)].append(s)
#         print(list(res.values()))



# arr = ["act", "god", "cat", "dog", "tac"]
# a=Solution()
# a.anagrams(arr)

# def rec(n):
#     if n<=1:
#         return 1
    
    
#     return n*rec(n-1)

# print(rec(5))










