#Valid Perfect Square	


class Solution:
    def is_perfect_square(self,n):
        if n<0:
            return False
        k=int(n**0.5)
        return k*k ==n


a=Solution()

print(a.is_perfect_square(0))      # True
print(a.is_perfect_square(1))      # True
print(a.is_perfect_square(4))      # True
print(a.is_perfect_square(9))      # True
print(a.is_perfect_square(16))     # True
print(a.is_perfect_square(25))     
print(a.is_perfect_square(34))
