# Odd-Even Vehicle Fine – Given last digits of N vehicles’ registration and a calendar date D, vehicles violate if odd-digit plates drive on even dates or vice versa. Each violation is fined X. Compute total fine.
# Description: Count vehicles with even last digit vs odd. If date D is odd, allowed are odd-digit vehicles (violations = count of even-digit vehicles). If D is even, allowed are even-digit (violations = count of odd). Total fine = violations * X ￼ ￼.
# Sample I/O:
# Input: N=4, a=[5,2,3,7], D=12, X=200 → Output: 600. (Date 12 is even, allowed evens; violators=3 vehicles (5,3,7 odd) → fine 3*200=600) ￼ ￼.
# Topic: Counting / Conditionals. Difficulty: Medium.


class Solution:
    def odd_v_fine(self,a,d,x):
        odd_c=0
        eve_c=0
        for i in a:
            if i%2==0:
                eve_c+=1
            else:
                odd_c+=1
        if d%2==0:
            return x*odd_c
        return x*eve_c
    

s = Solution()
print(s.odd_v_fine([5,2,3,7], 12, 200))   # Output: 600
print(s.odd_v_fine([1,3,5], 5, 100))      # odd date, odd allowed → even violators = 0 → output 0
print(s.odd_v_fine([2,4,6], 7, 50))       # odd date, odd allowed → all are violators → 3*50 = 150
print(s.odd_v_fine([9], 2, 500))          # even date, odd vehicle = violator → 500
print(s.odd_v_fine([], 10, 200))          # no vehicles → 0