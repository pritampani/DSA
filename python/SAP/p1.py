#Reverse a number

class Solution:
    def reverse_number(self,n):
        res=0
        while n>0:
            a=n%10
            res=res*10+a
            n//=10
        return res

a=Solution()
print(a.reverse_number(45678))
