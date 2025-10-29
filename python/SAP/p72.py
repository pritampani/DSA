#Generate all permutations
class Solution:
    def generate_per(self,s):
        res=[]
        idx=0
        s=list(s)
        self.helper(s,res,idx)
        return res
    def helper(self,s,res,idx):

        if idx==len(s):
            res.append(''.join(s))
            return
        


        seen=set()
        for i in range(idx,len(s)):
            if s[i] in seen:
                continue
            
            seen.add(s[i])
            s[i],s[idx]=s[idx],s[i]
            self.helper(s,res,idx+1)
            s[idx],s[i]=s[i],s[idx]

a = Solution()
print(a.generate_per("ABA"))
print(a.generate_per("ABC"))








