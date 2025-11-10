#Find Missing Number from 1..N


class Solution:
    def missing(self, arr):
        n = len(arr) + 1
        actual_sum = sum(arr)
        expected_sum = n * (n + 1) // 2
        return expected_sum - actual_sum


a = Solution()

print(a.missing([1,2,3,5]))          # Expected: 4
print(a.missing([2,3,1,5]))          # Expected: 4
print(a.missing([1]))                # Expected: 2
print(a.missing([2]))                # Expected: 1
print(a.missing([1,3,4,5,6]))        # Expected: 2
print(a.missing([2,4,1,3,6]))        # Expected: 5