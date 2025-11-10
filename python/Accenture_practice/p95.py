# 9. Find Minimum Element in Rotated Sorted Array

# Array is sorted but rotated; find the smallest element.

# Example:

# arr = [4,5,6,7,0,1,2] → Output: 0

# Concept: Binary search on rotated array.


class Solution:
    def find_min_binarysearch(self,arr):
        l=0
        r=len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[r]:
                l=mid+1
            else:
                r=mid
        return arr[l]

a = Solution()
print(a.find_min_binarysearch([4,5,6,7,0,1,2]))  # 0
print(a.find_min_binarysearch([3,4,5,1,2]))      # 1
print(a.find_min_binarysearch([11,13,15,17]))    # 11
print(a.find_min_binarysearch([2,1]))            # 1
print(a.find_min_binarysearch([1]))              # 1