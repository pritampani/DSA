#	1.	Given a string with letters and digits (e.g. "abc123de45f6"), 
# extract all numbers as integers → result [123, 45, 6].


class Soluton:
    def p1(self,s):
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
        return res

a=Soluton()
s='abc123de45f6'
print(a.p1(s))