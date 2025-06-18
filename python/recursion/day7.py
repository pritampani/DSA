#find all the subset of from the array
class Solution:
    def subset(self, arr):
        res = [[]]  
        for num in arr:
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])
            res.extend(new_subsets)  
        return res
a=Solution()
print(a.subset([1,2,3]))    