# Previous smaller elemmert

class Solution:
    def PSE(self,arr):
        res=[-1]*len(arr)
        stk=[]
        for i in range(len(arr)):
            while stk and stk[-1]>=arr[i]:
                stk.pop()
            if stk:
                res[i]=stk[-1]
            stk.append(arr[i])
        return res


a = Solution()
print(a.PSE([10, 4, 2, 20, 40, 12, 30]))