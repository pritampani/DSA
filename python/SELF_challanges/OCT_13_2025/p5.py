
# Given a string with words and numbers mixed, find the sum of all numbers in the string.

class Solution():
    def p5(self,s):
        
        c=0
        for i in range(len(s)):
            if s[i].isdigit():
                c+=int(s[i])

        return c

a=Solution()

s='jj222j4'
print(a.p5(s))