#4.	Minimum Value to Get Positive Step-by-Step Sum


class Solution:
    def minStartValue(self, nums):
        prefix = 0
        min_prefix = float('inf')

        for x in nums:
            prefix += x
            min_prefix = min(min_prefix, prefix)

        # start value must make min_prefix >= 1
        return 1 - min_prefix if min_prefix < 0 else 1
    
a=Solution()
print(a.minStartValue([-3,2,-3,4,2]))