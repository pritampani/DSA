# Given a CSV-like string (e.g. "12,abc,34,def,56"), split and extract numeric and non-numeric parts separately.


class Solution():
    def p4(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isdigit():
                if c!='' and c[-1].isalpha():
                    res.append(c)
                    c=''
                c+=s[i]
            if s[i].isalpha():
                if c!='' and c[-1].isdigit():
                    res.append(c)
                    c=''
                c+=s[i]
        if c!='':
            res.append(c)
        return res

a=Solution()

s='jj222j4'
print(a.p4(s))