#Binary Search (recursive)

class Solution:
    def binaryserch(self,arr,tar):
        l=0
        r=len(arr)-1
        return self.binary_helper(arr,tar,l,r)
    def binary_helper(self,arr,tar,l,r):
        if l>r:
            return False
        mid=(l+r)//2
        if arr[mid]==tar:
            return True
        if arr[mid]>tar:
            return self.binary_helper(arr,tar,l,mid-1)
        else:
            return self.binary_helper(arr,tar,mid+1,r)
        return False

a=Solution()
print(a.binaryserch([1,2,3,4,5,6,8,9],7))
