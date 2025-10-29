#Factorial using recursion



class Solution:
    def fact(self,n):
        if n==0 or n==1:
            return 1
        return n*self.fact(n-1)
    
a=Solution()
print(a.fact(5))
print(a.fact(4))
print(a.fact(6))