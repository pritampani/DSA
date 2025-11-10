#    Reverse a string



class Solution:
    def reverse_str(self,s)->str:
        res=''
        for i in range(len(s)-1,-1,-1):
            res+=s[i]
        return res
a=Solution()
print(a.reverse_str('chiku'))





