#Remove spaces from a string



class Solution:
    def remove_space(self,s)->str:
        res=''
        for i in range(len(s)):
            if s[i].isalpha():
                res+=s[i]
        return res

a=Solution()
print(a.remove_space(' my name is pritram pani who is preparing for SAP'))