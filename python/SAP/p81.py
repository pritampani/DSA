# Next smaller element

class Solution:
    def NSE(self,arr):
        res=[-1]*len(arr)
        stk=[]
        for i in range(len(arr)-1,-1,-1):
            while stk and stk[-1]>=arr[i]:
                stk.pop()
            
            if stk:
                res[i]=stk[-1]
            stk.append(arr[i])
        return res
a = Solution()
print(a.NSE([4, 8, 5, 2, 25]))