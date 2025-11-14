# Certainly. Here is the problem statement:

# Problem Statement

# Given an integer input n, which signifies the number of digits, find the minimum possible n-digit number that satisfies the following conditions:

# The sum of the squares of its digits is a perfect square.

# The number must not contain the digit zero (0).

# Example

# Input n = 3

# Output: 122

# Reason: The sum of the squares of the digits is 1 
# 2
#  +2 
# 2
#  +2 
# 2
#  =1+4+4=9.

# 9 is a perfect square (3²), and 122 is the minimum possible number that achieves this.

# Constraints

# n can be as large as 10 
# 6
#  .



class Solution:
    def issqrt(self, n):
        if n < 0:
            return False
        a = int(n**0.5)
        return a * a == n

    def magic(self, n):
        return self.helper(n, "", 0)

    def helper(self, digits_remaining, current_num_str, current_sum_sq):
        if digits_remaining == 0:
            if self.issqrt(current_sum_sq):
                return current_num_str
            else:
                return None

        for digit in range(1, 10):
            new_num_str = current_num_str + str(digit)
            new_sum_sq = current_sum_sq + (digit * digit)
            result = self.helper(digits_remaining - 1, new_num_str, new_sum_sq)
            if result is not None:
                return result
        return None

a=Solution()
print(a.magic(3))
print(a.magic(4))
print(a.magic(5))
print(a.magic(6))

