# Subset Sum Count – Given an array arr and an integer k, count subsets of arr whose sum is exactly k.
# Description: Count all combinations of elements summing to k (subset-sum count). 
# Example: arr=[1,2,3,4,5], k=5 has subsets {5},{1,4},{2,3}, total 3.
# Sample I/O:
# Input: arr=[1,2,3,4,5], k=5 → Output: 3. (Subsets [5], [1,4], [2,3]).
# Topic: Dynamic Programming / Recursion. Difficulty: Medium.

class Solution:
    def subset_sum(self,arr):
        dp=[[0]*(k+1) for _ in range(n+1)]
        for  i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(k+1):
                dp[i][j]=dp[i-1][j]
                if j>=arr[i-1]:
                    dp[i][j]+=dp[i-1][j-arr[i-1]]
        return ap[n][k]
    
a = Solution()

print(a.subset_sum([1,2,3,4,5], 5))       # Expected: 3 ([5], [1,4], [2,3])
print(a.subset_sum([1,2,3], 3))           # Expected: 2 ([3], [1,2])
print(a.subset_sum([2,4,6,10], 16))       # Expected: 2 ([6,10], [2,4,10])
print(a.subset_sum([1,1,1,1], 2))         # Expected: 6 (all combinations of two 1s)
print(a.subset_sum([1,2,3], 7))           # Expected: 0 (no subset sums to 7)
