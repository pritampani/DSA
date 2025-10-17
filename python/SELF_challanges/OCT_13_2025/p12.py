# Given a string with a decimal number like "The value is 12.34 and next is 56.7", extract decimal numbers.


class Solution:
    def p12(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isdigit() or s[i]=='.':
                c+=s[i]
            else:
                if c!='':
                    res.append(c)
                    c=''
        if c!='':
            res.append(c)
            c=''
        return res
a=Solution()
s="The value is 12.34 and next is 56.7"
print(a.p12(s))

                