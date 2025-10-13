# Given a string with key-value pairs like "x=123;y=456;z=789", parse to a map/dictionary.

class Solution:
    def p8(self, s):
        di = {}
        i = 0
        while i < len(s):
            if s[i].isalpha():
                key = s[i]
                i += 2  # skip '='
                value = ''
                while i < len(s) and s[i] != ';':
                    value += s[i]
                    i += 1
                di[key] = value
            i += 1
        return di


a = Solution()
s = "x=123;y=456;z=789"
print(a.p8(s))