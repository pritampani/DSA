# Find first and last occurrence using binary search

class Solution:
    def fas_last(self,arr,tar):
        a=self.fastoccurance(arr,tar)
        b=self.lastoccurance(arr,tar)
        return [a,b]
    def fastoccurance(self,arr,tar):
        l=0
        r=len(arr)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==tar:
                ans=mid
                r=mid-1
            elif arr[mid]>tar:
                r=mid-1
            else:
                l=mid+1
        return ans
    def lastoccurance(self,arr,tar):
        l=0
        r=len(arr)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==tar:
                ans=mid
                l=mid+1
            elif arr[mid]>tar:
                r=mid-1
            else:
                l=mid+1
        return ans

a=Solution()
print(a.fas_last([1,2,2,3,4,4,5,5,6,6,6,6,6,7,7],6))






