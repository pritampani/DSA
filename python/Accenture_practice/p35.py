#Find floor and ceil in sorted array
# arr = [1, 2, 4, 6, 10, 12]
# x = 5

# Now:
# 	•	Elements ≤ 5 → [1, 2, 4] → floor = 4
# 	•	Elements ≥ 5 → [6, 10, 12] → ceil = 6

# ✅ Output:
# floor = 4, ceil = 6


class Solution:
    def find_floor_ceil(self,arr,tar):
        l=0
        r=len(arr)-1
        floor=-1
        ceil=-1

        while l<=r:
            mid=(l+r)//2

            if arr[mid]==tar:
                return arr[mid],arr[mid]
            elif arr[mid]<tar:
                floor=arr[mid]
                l=mid+1
            else:
                ceil=arr[mid]
                r=mid-1
        return floor,ceil


# Example usage:
a = Solution()
print(a.find_floor_ceil([1, 2, 4, 6, 10, 12], 5))   # Output: (4, 6)
print(a.find_floor_ceil([1, 2, 4, 6, 10, 12], 10))  # Output: (10, 10)
print(a.find_floor_ceil([1, 2, 4, 6, 10, 12], 0))   # Output: (-1, 1)