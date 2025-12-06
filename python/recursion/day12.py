#check the array is sorted or not?? using recursion



class Solution:
    def issorted(self,arr,n):
        if n==0:
            return True
        return self.helper(arr,n,0)
    def helper(self,arr,n,i):
        if i==len(arr)-1:
            return True
        
        if arr[i]>arr[i+1]:
            return False
        
        else:
            remaningpart=self.helper(arr,n-1,i+1)
            return remaningpart

a=Solution()
print(a.issorted([1,2,3,4,5],5))   # True
print(a.issorted([1,2,3,9,5],5))   # False
print(a.issorted([],0))            