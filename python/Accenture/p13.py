# Remove Duplicates From Sorted Array
# Remove Duplicates from Sorted Array – Given a sorted array, remove duplicates in-place so 
# that each element appears only once; return the new length and array prefix of unique elements.
# Description: Iterate and copy unique elements to the front (two-pointer method) ￼. 
# For example, [1,2,2,3,4,4,5] becomes [1,2,3,4,5] plus don’t-care values after index.
# Sample I/O:
# Input: [1,2,2,3,4,4,4,5,5] → Output (distinct prefix): [1,2,3,4,5] (length 5) ￼.
# Topic: Arrays (In-place). Difficulty: Easy.


class Solution:
    def remove_dup(self, arr):
        if not arr:
            return arr

        pos = 0
        for i in range(1, len(arr)):
            if arr[pos] != arr[i]:
                pos += 1
                arr[pos] = arr[i]

        # Optional: fill the rest with 0
        for i in range(pos + 1, len(arr)):
            arr[i] = 0

        return arr

a=Solution()
print(a.remove_dup([1,2,2,3,4,4,4,5,5]))
