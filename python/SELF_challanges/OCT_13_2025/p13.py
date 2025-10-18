# Given a string of words and punctuation, find the longest word (exclude punctuation).

"""
Input
"Artificial intelligence is revolutionizing everything!"
Expected Output
"revolutionizing"
"""
#tc=O(n)
#AS=O(n)
# class Solution:
#     def p13(self,s):
#         k=s.split(' ')
#         mxstr=''
#         for i in range(len(k)):
#             if len(k[i])>len(mxstr):
#                 mxstr=k[i]
#         return mxstr
# a=Solution()
# s="Artificial intelligence is revolutionizing everything!"
# print(a.p13(s))


# tc=O(n)
# AS=O(1)

class Solution:
    def p13(self,s):
        
        mxstr=''
        i=0
        curr=''
        while i<len(s):
            if s[i].isalpha():
                curr+=s[i]
                i+=1
            else:
                if curr!='' and len(curr)>len(mxstr):
                    mxstr=curr
                    curr=''
                    
                curr=''
                i+=1



        return mxstr
a=Solution()

s="Artificial intelligence is revolutionizing everythingdfgssefgfg!"
print(a.p13(s))