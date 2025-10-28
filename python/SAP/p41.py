#Find union of two arrays


class Solution:
    def uninou(self,a,b):
        seen=set(a)
        for i in range(len(b)):
            if b[i] not in seen:
                seen.add(b[i])
        res=[]
        for i in seen:
            res.append(i)
        return res

a=Solution()
print(a.uninou([1,2,3,4,5],[1,2,3,4,66,7,8]))





