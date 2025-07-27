#User function Template for python3
# TC=O(N)
# AS=O(1)
class Solution:
    def getCount(self,s, n):
           
        freq=[0]*26
        prev=''
        for i in range(len(s)):
            if s[i]!=prev:
                freq[abs(ord(s[i])-ord('a'))]+=1

            prev=s[i]
        c=0
        seen=set()
        for i in range(len(s)):
            if freq[ord(s[i])-ord('a')]==n and s[i] not in seen:
                c+=1
                seen.add(s[i])
        return c

       
# TC=O(N)
# AS=O(N)     
class Solution:
    def getCount (self,s, n):
        freq={}
        prev=''
        for i in range(len(s)):
            if s[i]!=prev:
                freq[s[i]] = freq.get(s[i], 0) + 1
            prev=s[i]
        c=0
        seen=set()
        for i in range(len(s)):
            if freq[s[i]]==n and s[i] not in seen:
                c+=1
                seen.add(s[i])
                
                
        return c

a=Solution()
print(a.getCount('geeksforgeeks'))