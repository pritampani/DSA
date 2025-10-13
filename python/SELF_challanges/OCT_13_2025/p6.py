#. Given a string with parentheses containing numbers, e.g. "a(123)b(4567)c", extract numbers inside parentheses.

class Solution:
    def p6(self, s):
        res = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                c = ''
                while s[i].isdigit():
                    c += s[i]
                    i += 1
                res.append(c)
            else:
                i += 1
        return res

a = Solution()
s = "a(123)b(4567)c34"
print(a.p6(s))