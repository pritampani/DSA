#print all subsequence using resursion

class Solution:
    def prinntallsubsequence(self,s):
        curr=[]
        res=[]
        self.helper(s,0,curr,res)
        return res
    def helper(self,s,i,curr,res):

        if i==len(s):
            res.append(''.join(curr[:]))
            return
        
        curr.append(s[i])
        print(i)
        self.helper(s,i+1,curr,res)
        
        curr.pop()
        self.helper(s,i+1,curr,res)
#main
a=Solution()
print(a.prinntallsubsequence('312'))