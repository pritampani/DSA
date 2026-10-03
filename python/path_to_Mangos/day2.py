class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[]
        longest=-1
        curr=0
        for i in range(len(s)):
            print(stk)
            
            if s[i]=='(':
                stk.append(s[i])
            elif s[i]==')' and (len(stk)!=0 and stk[-1]=='('):
                curr+=2
                longest=max(longest,curr) 
                stk.pop()
            else:
                curr=0
                
        return longest 

a=Solution()
s=")()())"
print(a.longestValidParentheses(s))