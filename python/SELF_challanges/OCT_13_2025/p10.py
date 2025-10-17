# Given a string with roman numerals embedded, e.g. "abcXIIefV", extract and convert them to integers.


class Solution:
    def romantoint(self,s):
        def value(c):
            if c=='I':
                return 1
            if c=='V':
                return 5
            if c=='X':
                return 10 
            if c=='L':
                return 50
            if c=='C':
                return 100
            if c=='D':
                return 500
            if c=='M':
                return 1000
            return -1
        	
        res=0
        i = 0
        while i < len(s):
            s1 = value(s[i])

            if i + 1 < len(s):
                s2 = value(s[i + 1])
                # if current value is greater or equal, 
                # add it to result
                if s1 >= s2:
                    res += s1
                else:
                    # else, add the difference and 
                    # skip next symbol
                    res += (s2 - s1)
                    i += 1
            else:
                res += s1
            i += 1

        return res

    def sting_process(self,s):
        res=[]
        c=''
        for i in range(len(s)):
            if s[i].isupper():
                c+=s[i]
            else:
                if c!='':
                    k=self.romantoint(c)
                    res.append(k)
                    c=''
        if c!='':
            k=self.romantoint(c)
            res.append(k)
            c=''
        return res
a= Solution()
s="abcXIIefV"
print(a.sting_process(s))
