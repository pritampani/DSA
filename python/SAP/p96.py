# 10. Search Element in Rotated Sorted Array

# Given rotated sorted array, find target index.

# Example:

# arr = [4,5,6,7,0,1,2], target=0 → Output: 4

# Concept: Divide search space into sorted halves.



class Solution:
    def search_rotated(self,arr,x):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return mid
            if arr[mid]>=arr[l]:
                if arr[l]<=x <arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<x<=arr[r]:
                    l=mid+1
                else:
                    r=mid+1
        return -1
    
a = Solution()

print(a.search_rotated([4,5,6,7,0,1,2], 0))   # 4
print(a.search_rotated([4,5,6,7,0,1,2], 3))   # -1
print(a.search_rotated([1], 0))               # -1
print(a.search_rotated([1], 1))               # 0
print(a.search_rotated([6,7,1,2,3,4,5], 6))   # 0
print(a.search_rotated([6,7,1,2,3,4,5], 3))   # 4
print(a.search_rotated([5,1,3], 3))           # 2