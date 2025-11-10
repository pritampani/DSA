# Check Power of Two


class Solution:
    def is_power_of_two(self,n):
        return n>0 and (n&(n-1))==0

a = Solution()

print(a.is_power_of_two(16))   # True (Yes)
print(a.is_power_of_two(18))   # False (No)
print(a.is_power_of_two(1))    # True (2^0)
print(a.is_power_of_two(0))    # False
print(a.is_power_of_two(64))   # True