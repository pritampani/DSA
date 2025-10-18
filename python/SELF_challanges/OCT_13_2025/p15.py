#Given a string, find the first non-repeating character.




class Solution:
    def p15(self,s)->str:
        fre=dict()
        for i in s:
            fre[i]=fre.get(i,0)+1
        
        for j in fre:
            if fre[j]==1:
                return j
        return -1

a=Solution()
print(a.p15("geeksforgeeks"))
