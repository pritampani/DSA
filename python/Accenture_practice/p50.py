#Count 1s in sorted binary array


class Solution:
    def count1(self,arr):
        l=0
        r=len(arr)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==1:
                ans=mid
                l=mid+1
            elif arr[mid]>1:
                r=mid-1
            else:
                l=mid+1
        return ans+1
    
a= Solution()
print(a.count1([1,1,2,2,2,3,3]))