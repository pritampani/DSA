# Given a string of words and punctuation, find the longest word (exclude punctuation).

"""
Input
"Artificial intelligence is revolutionizing everything!"
Expected Output
"revolutionizing"
"""

class Solution:
    def p13(self,s):
        k=s.split(' ')
        mxstr=''
        for i in range(len(k)):
            if len(k[i])>len(mxstr):
                mxstr=k[i]
        return mxstr
a=Solution()

s="Artificial intelligence is revolutionizing everything!"
print(a.p13(s))