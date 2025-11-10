# Diamond pattern

class Solution:
    def diamond_partten(self,n):

        for i in range(1,n):
            print(" "*(n-i)+"*"*(2*i-1))
        for j in range(n-2,-1,-1):
            print(' '*(n-j)+'*'*(2*j-1))

a=Solution()
a.diamond_partten(7)
