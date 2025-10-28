#Count digits in a number


class Solution:
    def count_num(self,n):
        c=0
        
        while n>0:
            c+=1
            n//=10
        return c


a=Solution()
print(a.count_num(1234))