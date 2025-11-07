#GCD of Two Numbers

class Solution:
    def GCD(self,x,y):
        while y!=0:
            x,y=y,x%y
        return x



a = Solution()

print(a.GCD(10, 15))    # Expected: 5
print(a.GCD(21, 14))    # Expected: 7
print(a.GCD(17, 13))    # Expected: 1
print(a.GCD(100, 25))   # Expected: 25
print(a.GCD(0, 5))      # Expected: 5
print(a.GCD(5, 0))      # Expected: 5
print(a.GCD(0, 0))      # Expected: 0

