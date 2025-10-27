# 17.Find all starting indices where a pattern occurs.
# "ababcabcababc", "abc"
# [2, 5, 10]
class Solution:
        def p17(self,s,p):
                res=[]
                for i in range(len(s)):
                        if s[i:i+len(p)]==p:
                                res.append(i)
                return res
                                

                
a=Solution()
print(a.p17("ababcabcababc", "abc"))