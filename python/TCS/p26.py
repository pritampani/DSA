#Count Set Bits (Hamming Weight) – Count the number of 1’s in the binary representation of an integer n.
# Description: Repeatedly n &= (n-1) or use built-in; count operations.
# Sample I/O:
# Input: n=11 (binary 1011) → Output: 3.
# Topic: Bitwise. Difficulty: Easy. (Classic bit manipulation)


class Solution:
    def count_set_bit(self,n):
        b=bin(n)[2:]
        d=b.count('1')
        return d

#✅ Optimal Solution Using Bit Manipulation (Brian Kernighan’s Algorithm)
class Solution:
    def count_set_bit(self, n):
        count = 0
        while n:
            n &= (n - 1)  
            count += 1
        return count

a = Solution()

print(a.count_set_bit(11))   # 1011 → 3
print(a.count_set_bit(0))    # 0 → 0
print(a.count_set_bit(1))    # 1 → 1
print(a.count_set_bit(15))   # 1111 → 4
print(a.count_set_bit(16))   # 10000 → 1