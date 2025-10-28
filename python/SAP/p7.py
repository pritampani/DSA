#Fibonacci series



class Solution:
    def fibo_nacciseries(self,n):
        if n==0 or n==1:
            return n
        return self.fibo_nacciseries(n-1)+self.fibo_nacciseries(n-2)


a=Solution()
print(a.fibo_nacciseries(7))

