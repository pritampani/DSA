# find the frequency of an array without using map or dictinary or set 

class Solution:
    def freq(self,s):
        freq=[0]*26

        for i in s:
            if i==' ':
                continue
            freq[ord(i)-ord('a')]+=1
        return freq

a=Solution()
print(a.freq('pritam pani abc'))

