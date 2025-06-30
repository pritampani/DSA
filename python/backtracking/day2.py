# from typing import List
# class Solution:
#     def permute(self, arr: List[int]) -> List[List[int]]:
#         res=[]
#         i=0
#         self.helper(arr,i,res)
#         return res
#     def helper(self,arr,i,res):
#         #basecase??
#         if i==len(arr):
#             res.append(arr[:])
#             return



#         for idx in range(i,len(arr)):
#             arr[i],arr[idx]=arr[idx],arr[i]
#             self.helper(arr,i+1,res)
#             arr[i],arr[idx]=arr[idx],arr[i]

# a=Solution()
# print(a.permute([1,2,3]))
# print(a.permute([1,2]))