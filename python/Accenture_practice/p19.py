#Find frequency of each character

class Solution:
    def freq(self,s):
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        return d

a= Solution()
print(a.freq('aabcdefghijk;mnopqrstuvwxyz'))


