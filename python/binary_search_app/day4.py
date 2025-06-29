# return number of element perent in the array less than ot equal to x
class Solution:
    def binaryser(self,arr,x):
        if len(arr)==0:
            return -1
        l=0
        r=len(arr)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]<=x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans+1

a=Solution()
print(a.binaryser([1,2,3,4,5,6,7],4))
print(a.binaryser([1,2,3,4,5,6,7],4))
print(a.binaryser([1,2,3,4,5,6,7],6))
print(a.binaryser([1,2,3,4,5,6,7],7))
print(a.binaryser([],4))


#1498. Number of Subsequences That Satisfy the Given Sum Condition



