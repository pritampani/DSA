#. Given a string representing a nested structure like "[1,2,[3,4],5]", parse it into a nested list / array.

class Solution():
    def p3(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isdigit() or s[i]=='-':
                c+=s[i]
            else:
                if c!='':
                    res.append(c)
                    c=''
        if c!='':
            res.append(c)
        return res

a=Solution()

s="Today is 2025-10-13 and tomorrow is 2025-10-14"

print(a.p3(s))