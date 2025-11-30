class Solution:
    def find_anagram(self,s1,s2):
        has=[0]*123
        for i in range(len(s1)):
            has[ord(s1[i])]+=1
        for i in range(len(s2)):
            has[ord(s2[i])]-=1
        
        for i in range(len(has)):
            if has[i]!=0:
                return False
        return True
a=Solution()
s = "listen"
t = "Silent"
print(a.find_anagram(s,t))
