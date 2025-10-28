#Find factorial of a number

class Solution:
    def allfactioal(self,n):
        res=[]
        for i in range(1,n):
            if n%i==0:
                res.append(i)
        return res

a=Solution()

print(a.allfactioal(12))