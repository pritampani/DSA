#Sum of digits


class Solution:
    def sum_num(self,n):
        res=0

        while n>0:
            res+=n%10
            n//=10
        return res

a=Solution()

print(a.sum_num(123))




