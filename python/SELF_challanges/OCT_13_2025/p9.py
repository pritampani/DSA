# Given a string with “ranges” like "1-5,10-12,20-20", expand them to list of numbers: [1,2,3,4,5,10,11,12,20].



class Solution:
    def p9(self, s):
        res = []
        parts = s.split(',')           
        for part in parts:
            a, b = part.split('-')    
            a, b = int(a), int(b)
            res += self.rangearray(a, b)
        return res

    def rangearray(self, a, b):
        return [i for i in range(a, b + 1)] 

a = Solution()
s = "1-5,10-12,20-20"
print(a.p9(s))