# Count Elements Greater Than All Previous – Count how many elements in an array are strictly greater than every element to their left. Include the first element by default.
# Description: Given array Arr, an element qualifies if it’s larger than all prior elements. By convention, the first element counts (no prior elements) ￼ ￼.
# Sample I/O:
# Input: N=5, Arr=[7,4,8,2,9] → Output: 3 (elements 7, 8, 9 satisfy). ￼ ￼
# Topic: Arrays / Scanning. Difficulty: Easy.


class Solution:
    def count_greater(self,arr):
        if not arr:
            return 0
        
        maxi=arr[0]
        c=1
        for i in range(1,len(arr)):
            if arr[i]>maxi:
                c+=1
                maxi=arr[i]
        return c
    

s = Solution()
print(s.count_greater([7, 4, 8, 2, 9]))  # Output: 3