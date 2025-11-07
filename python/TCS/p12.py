# 	12.	Second Largest in Array – Find the second largest distinct element in an array of integers. If none exists, indicate so.
# Description: Scan the array to track the largest and second-largest values ￼. If all elements equal, report no second largest.
# Sample I/O:
# Input: arr=[13,14,15,16,17,18] → Output: 17. (Largest is 18, second largest is 17) ￼.
# Topic: Arrays. Difficulty: Easy.



class Solution:
    def p12(self,arr):
        f=float('-inf')
        s=float('-inf')
        for i in range(len(arr)):
            if arr[i]>f:
                s=f
                f=arr[i]
            elif arr[i]>s and arr[i]!=f:
                s=arr[i]
        return s


a = Solution()

# 1. Strictly increasing array
print(a.p12([13, 14, 15, 16, 17, 18]))   # Expected: 17

# 2. Random mixed values
print(a.p12([5, 1, 9, 3, 7]))           # Expected: 7

# 3. Largest number at start
print(a.p12([10, 9, 8, 7]))             # Expected: 9

# 4. Largest number at end
print(a.p12([4, 2, 1, 10]))             # Expected: 4

# 5. Array with duplicates of largest
print(a.p12([10, 10, 9, 8]))            # Expected: 9

# 6. Array with all elements equal
print(a.p12([5, 5, 5, 5]))              # Expected: "No second largest"

# 7. Only 1 element
print(a.p12([7]))                       # Expected: "No second largest"

# 8. Negative numbers
print(a.p12([-5, -1, -10, -3]))         # Expected: -3

# 9. Mixed positive + negative
print(a.p12([-1, 0, 3, 2]))             # Expected: 2

# 10. Second largest is negative
print(a.p12([-10, -20, -30]))           # Expected: -20

