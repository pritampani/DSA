#Binary Search (iterative)

class Solution:
    def binary_search(self,arr,target):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1

a=Solution()
print(a.binary_search([1,2,3,4,5,6,7,8,9],7))

