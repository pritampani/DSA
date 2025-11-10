#Maximum Subarray Sum (Kadane’s Algorithm)


class Solution:
    def max_sum(self,arr):
        cs=0
        maxi=arr[0]
        for i in range(len(arr)):
            cs+=arr[i]
            maxi=max(cs,maxi)
            if cs<=0:
                cs=0

        return maxi

a = Solution()

print(a.max_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]))  # Expected: 9 ([3,4,-1,2,1])
print(a.max_sum([-2, -3, -1, -5]))               # Expected: -1 (single largest element)
print(a.max_sum([5, 4, -1, 7, 8]))               # Expected: 23
print(a.max_sum([1]))                             # Expected: 1
print(a.max_sum([-1]))                            # Expected: -1

