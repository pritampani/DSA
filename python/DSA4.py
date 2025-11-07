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




# class Solution:
#     def min_house(self,r,unit,arr):
#         if len(arr)==0:
#             return -1

#         if sum(arr)<r*unit:
#             return -1
        
#         s=0
#         requirment=r*unit
#         for i in arr:
#             s+=i
#             if s>=requirment:
#                 return i





class Solution:
    def kapkar(self,n,d):
        res=[]
        for i in range(d,n+1):
            if self.iskapka(i)==self.iskapka(i*i):
                res.append(i)
        return res


    def iskapka(self,n):
        s=0
        while n>0:
            d=n%10
            s+=d
            n//=10
        return s
    

a=Solution()
print(a.kapkar(100,1))

