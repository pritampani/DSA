#Check Palindrome String


class Solution:
    def palandrom(self,s):
        return s==s[::-1]


a = Solution()

print(a.palandrom("racecar"))   # True
print(a.palandrom("level"))     # True
print(a.palandrom("hello"))     # False
print(a.palandrom("a"))         # True
print(a.palandrom(""))          # True