# Given a string, find the longest substring without repeating characters.


class Solution:
    def p16(self,s):
        seen=set()
        res=''
        left=0
        maxi=0
        start=0
        

        for r in range(len(s)):
            if s[r] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[r])
            win=(r-left)+1
            if win>maxi:
                maxi=win
                start=left
        return s[start:start+maxi]

obj = Solution()
print(obj.p16("abcabcbb"))
