#Find element in infinite sorted array

class Solution:
    def search_infinite(self,arr,x):
        l=0
        r=len(arr)-1


        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return mid
            if arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return -1

a=Solution()
print(a.search_infinite([1,2,3,4,4,7,7,8,8],3))
