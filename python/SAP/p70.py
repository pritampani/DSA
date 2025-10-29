#Fibonacci using recursion


class Solution:
    def fibo(self,n):
        if n==0 or n==1:
            return n
        return self.fibo(n-1)+self.fibo(n-2)

a=Solution()
print(a.fibo(0))
print(a.fibo(1))
print(a.fibo(2))
print(a.fibo(3))
print(a.fibo(4))
print(a.fibo(5))
print(a.fibo(6))
print(a.fibo(7))