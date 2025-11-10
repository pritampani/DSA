# 7. Search Insert Position

# Given a sorted array and a target, return the index if the target is found.
# If not, return the index where it would be inserted to keep the array sorted.

# Example:

# arr = [1, 3, 5, 6]
# x = 5 → Output: 2
# x = 2 → Output: 1

# Concept: Binary search variant.


class Solution:
    def insert_binary_serch(self,arr,x):
        l,r=0,len(arr)-1

        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return mid
            elif arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        return l
    
a = Solution()
print(a.insert_binary_serch([1, 3, 5, 6], 5))  # 2
print(a.insert_binary_serch([1, 3, 5, 6], 2))  # 1
print(a.insert_binary_serch([1, 3, 5, 6], 7))  # 4
print(a.insert_binary_serch([1, 3, 5, 6], 0))  # 0