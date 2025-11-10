#Print all subsequences of string

class Solution:
    def print_subsequence(self,s):
        i=0
        res=[]
        curr=[]
        self.helper(s,i,res,curr)
        return res
    def helper(self,s,i,res,curr):

        if i==len(s):
            res.append(''.join(curr))
            return



        curr.append(s[i])
        self.helper(s,i+1,res,curr)
        curr.pop()
        self.helper(s,i+1,res,curr)



a=Solution()
print(a.print_subsequence('abc'))
