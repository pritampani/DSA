#Armstrong number check




class Solution:
    def armstromenumber(self,n)->bool:
        a=n
        c=0
        while a>0:
            c+=1
            a//=10
        
        b=n
        res=0
        while b>0:
            d=b%10
            res+=d**c
            b//=10
        return res==n

a=Solution()
print(a.armstromenumber(153))






