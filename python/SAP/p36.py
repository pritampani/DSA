#Find missing number in 1 to N

class Solution:
    def missing_number(self,arr):
        asum=0
        n=max(arr)
        for i in arr:
            asum+=i
        ps=n*(n+1)//2
        return ps-asum

a=Solution()
print(a.missing_number([1,2,3,5]))
        








