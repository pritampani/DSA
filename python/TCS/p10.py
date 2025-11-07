# Max ‘a’ Count in Fixed-Size Substrings – A string of ‘a’/‘b’ curtains of length N is divided 
# into boxes each containing L curtains 
# (last box may have ≤L). Find the box with the most ‘a’ characters, and output that count.
# Description: Divide the string into contiguous substrings of length L. 
# Count ‘a’ in each box. Return the maximum count of ‘a’ among all boxes ￼ ￼.
# Sample I/O:
# Input: str="bbbaaababa", L=3 → Output: 3 (the box aaa has 3 ‘a’s) ￼ ￼.
# Topic: Strings. Difficulty: Medium.


class Solution:
    def maxainbox(self,s,l):
        mx=0
        for i in range(0,len(s),l):
            box=s[i:i+l]
            mx=max(mx,box.count('a'))
        return mx

s = Solution()
print(s.maxainbox("bbbaaababa", 3))  # Output: 3