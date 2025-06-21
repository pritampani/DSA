#1.23
# class Solution:
#     def checkoutofbound(self,arr,ele,idx):
#         if idx>=len(arr):
#             return 'Dont Try buffer overflow attack in python'
        
#         for i in range(idx, len(arr)):
#             if arr[i] == ele:
#                 return i
        
#         return 'Element not found from given index'


# s = Solution()
# print(s.checkoutofbound([1,2,3,4,5], 4, 2))  # Output: 3
# print(s.checkoutofbound([1,2,3,4,5], 6, 2))  # Output: 'Element not found from given index'
# print(s.checkoutofbound([1,2,3], 2, 5))      # Output: 'Index out of bounds'





#1.24

# class Solution:
#     def countvowle(self,s):
#         c=0
#         for i in s:
#             if i in ('a','e','i','o','u','A','E','I','O','U'):
#                 c+=1
#         return c
# a=Solution()
# print(a.countvowle('aeoiuAEIOUsdfghjklzxvbnm')) #10






#1.25

# class Solution:
#     def removeallpunctutions(self,s):
#         res=''
#         for i in range(len(s)):
#             if s[i] in (',',';',"'",'.'):
#                 continue
#             res+=s[i]
#         return res
# a=Solution()
# print(a.removeallpunctutions("let's try, Mike."))


























