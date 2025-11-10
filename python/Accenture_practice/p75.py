#Palindrome partitioning


class Solution:
    def palandrom_parti(self,s):
        res=[]
        curr=[]
        i=0
        self.helper(s,res,curr,i)
        return res
    def helper(self,s,res,curr,start):

        if start==len(s):
            res.append(curr[:])
            return
        


        for end in range(start+1,len(s)+1):
            subset=s[start:end]
            if subset==subset[::-1]:
                curr.append(subset)
                self.helper(s,res,curr,end)
                curr.pop()
        

a = Solution()
print(a.palandrom_parti("aab"))
print(a.palandrom_parti("geeks"))
print(a.palandrom_parti("abcba"))
print(a.palandrom_parti("aaa"))
print(a.palandrom_parti("racecar"))
print(a.palandrom_parti("abba"))
print(a.palandrom_parti("abc"))
print(a.palandrom_parti("a"))
print(a.palandrom_parti("noon"))
print(a.palandrom_parti("level"))