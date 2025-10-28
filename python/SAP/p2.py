#Check if a number is palindrome




class Solution:
    def check_palandrom(self,n):
        a=n
        res=0
        while a>0:
            d=a%10
            res=res*10+d
            a//=10
        return n==res
a=Solution()
print(a.check_palandrom(1213))