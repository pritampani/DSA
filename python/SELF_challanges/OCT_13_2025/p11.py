# Given a string with HTML-like tags: "<div>123</div><p>456</p>", extract numbers inside tags.



class Solution:
    def p11(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isdigit():
                c+=s[i]
            else:
                if c!='':
                    res.append(c)
                    c=''
        if c!='':
            res.append(c)
            c=''
        return res

a= Solution()
s="<div>123</div><p>456</p>"
print(a.p11(s))


