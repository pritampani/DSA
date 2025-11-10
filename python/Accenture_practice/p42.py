#Count pairs with given sum


class Solution:

    def countPairs(self,arr, target):
        d={}
        count=0
        for i in arr:
            if target-i in d:
                count+=d[target-i]
            d[i]=d.get(i,0)+1
        return count       

a=Solution()
print(a.countPairs([1,2,3,4,66,7,8],5))
print(a.countPairs([1, 1, 1, 1],2))

