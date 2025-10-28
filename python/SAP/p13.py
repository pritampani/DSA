# Pyramid pattern




class Solution:
    def pyrimid(self,n):
        for i in range(1,n):
            print(" "*(n-i)+"*"*(2*i-1))

a=Solution()
a.pyrimid(7)