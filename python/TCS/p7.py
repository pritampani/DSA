#Product of Digits of a Number


class Solution:
    def pro_digit(self,n):
        p=1
        while n>0:
            p*=n%10
            n//=10
        return p


a=Solution()
print(a.pro_digit(987654321))