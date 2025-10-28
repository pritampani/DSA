#Power of a number without using pow()




class Solution:
    def power(self,n,expo):
        res=1
        for i in range(expo):
            res*=n
        return res

a=Solution()
print(a.power(2,3))

