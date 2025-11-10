#Find GCD & LCM of two numbers


class Solution:
    def GCD_LCM(self,a,b):
        x=a
        y=b

        while y:
            x,y=y,x%y
        lcm=(a*b)//x
        return x, lcm


a=Solution()
print(a.GCD_LCM(12,18))




