#. Given a string containing dates like "Today is 2025-10-13 and tomorrow is 2025-10-14", extract the dates.


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