# 8. Find First and Last Occurrence of Target

# Given sorted array, find first and last index of a given element (without counting frequency directly).

# Example:

# arr = [2, 4, 4, 4, 5, 6]
# target = 4 → Output: [1, 3]

# Concept: Modified binary search.

# ⸻


class Solution:
    def first_and_last_occurrence(self, arr, x):
        first = self.first_occ(arr, x)
        last = self.last_occ(arr, x)
        return [first, last]

    def first_occ(self, arr, x):
        l, r = 0, len(arr) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                ans = mid
                r = mid - 1     
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def last_occ(self, arr, x):
        l, r = 0, len(arr) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                ans = mid
                l = mid + 1    
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        return ans



a = Solution()

print(a.first_and_last_occurrence([2, 4, 4, 4, 5, 6], 4))  # [1, 3]
print(a.first_and_last_occurrence([1, 2, 3, 4, 5], 3))     # [2, 2]
print(a.first_and_last_occurrence([1, 2, 3, 4, 5], 6))     # [-1, -1]
print(a.first_and_last_occurrence([1, 1, 1, 1, 1], 1))     # [0, 4]
print(a.first_and_last_occurrence([1, 2, 3, 4, 5], 1))     # [0, 0]
print(a.first_and_last_occurrence([], 5))                  # [-1, -1]