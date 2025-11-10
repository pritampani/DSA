# Count Subarrays with Given Sum – Given an array of integers and target sum, 
# count how many contiguous subarrays sum to sum.
# Description: Return the number of subarrays (contiguous) whose elements add up exactly to sum. 
# (Classic “subarray sum equals K” problem) ￼.
# Sample I/O:
# Input: arr=[1,1,1], sum=2 → Output: 2 (subarrays [1,1] at positions (1-2) and (2-3)).
# Topic: Arrays, Two-pointer/Hashing. Difficulty: Medium ￼.


class Solution:
    def p11(self,arr,k):
        prifix_sum=0
        count=0
        freq={0:1}
        for x in arr:
            prifix_sum+=x
            if prifix_sum-k in freq:
                count+=freq[prifix_sum-k]
            freq[prifix_sum]=freq.get(prifix_sum,0)+1
        return count


a = Solution()


print(a.p11([1, 1, 1], 2))   # Expected: 2

# 2. All positive numbers
print(a.p11([2, 3, 5, 1, 1], 6))   # Expected: 2

# 3. With negative numbers
print(a.p11([1, -1, 1, -1, 1], 1))   # Expected: 5

# 4. Contains zero values
print(a.p11([0, 0, 0], 0))   # Expected: 6

# 5. Large mix
print(a.p11([3, 4, -7, 1, 3, -2, 1, 4, 2], 7))   # Expected: 4

# 6. Entire array forms sum
print(a.p11([2, 4, 3, 1], 10))   # Expected: 1

# 7. No match
print(a.p11([5, 6, 7], 1))   # Expected: 0

# 8. Single element
print(a.p11([5], 5))   # Expected: 1
print(a.p11([5], 10))  # Expected: 0

# 9. Repeated values
print(a.p11([1, 2, 1, 2, 1], 3))   # Expected: 4

# 10. Pos + neg cancel
print(a.p11([10, -10, 10, -10, 10], 0))   # Expected: 4