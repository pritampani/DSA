# Round-Table Seating (Adjacent Leaders) – In a round-table seating of N people, two specific persons (e.g., President and PM) must sit together. Count possible seatings.
# Description: Treat the pair as one unit (they can swap among themselves: 2! ways), then arrange (N-1)! remaining positions. Total = 2*(N-1)! ￼ ￼.
# Sample I/O:
# Input: 4 (persons) → Output: 12. (Calculation: 2 * 3! = 12) ￼.
# Topic: Combinatorics (Factorial). Difficulty: Medium.



class Solution:
    def round_table(self,n):
        p=1
        for i in range(1,n):
            p*=i
        return p*2

s = Solution()
print(s.round_table(4))  # Output: 12
