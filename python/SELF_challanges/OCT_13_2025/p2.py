
# Given a string that has numbers possibly with signs (e.g. "a-12b+34c-5"), extract signed integers: [-12, +34, -5].



class Solution:
    def p2(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isdigit() or s[i]=='+' or s[i]=='-':
                c+=s[i]
            else:
                if c!='':
                    res.append(c)
                    c=''
        if c!='':
            res.append(c)
        return res

a=Solution()
s="a-12b+34c-5"
print(a.p2(s))