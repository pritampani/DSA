from typing import List
class Solution:
    def combine(self, n: int, k: int):
        res=[]
        curr=[]
        i=0
        arr=list(range(1,n+1))
        self.helper(arr,i,res,curr,k)
        return res


    def helper(self,arr,i,res,curr,k):

        if len(curr)==k:
            res.append(curr[:])
            return 
        if i==len(arr):
            return 

        curr.append(arr[i])
        self.helper(arr,i+1,res,curr,k)
        curr.pop()
        self.helper(arr,i+1,res,curr,k)

a=Solution()
print(a.combine(4,2))
print(a.combine(4,3))
print(a.combine(4,1))