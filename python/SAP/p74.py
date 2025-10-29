#Combination sum


class Solution:
    def combi_sum(self,arr,tar):
        res=[]
        curr=[]
        i=0
        self.helper(arr,tar,res,curr,i)
        return res
    def helper(self,arr,tar,res,curr,i):

        if tar==0:
            res.append(curr[:])
            return
        if i==len(arr) or tar<0:
            return

        

        curr.append(arr[i])
        self.helper(arr,tar-arr[i],res,curr,i)
        curr.pop()
        self.helper(arr,tar,res,curr,i+1)
a = Solution()

print(a.combi_sum([2, 3, 6, 7], 7))
print(a.combi_sum([2, 3, 5], 8))
print(a.combi_sum([2], 1))
print(a.combi_sum([1], 2))
print(a.combi_sum([], 3))
print(a.combi_sum([1, 2, 3], 4))
print(a.combi_sum([2, 4, 8], 8))
print(a.combi_sum([3, 4, 5], 9))
print(a.combi_sum([2, 5, 10], 20))
print(a.combi_sum([1, 7], 7))