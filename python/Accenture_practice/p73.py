#Subset sum problem

class Solution:
    def subset_sum(self,arr,tar):
        i=0
        return self.helper(arr,tar,i)
    def helper(self,arr,tar,i):
        if tar==0:
            return True
        if i==len(arr) or tar<0:
            return False


        
        include=self.helper(arr,tar-arr[i],i+1)
        exclude=self.helper(arr,tar,i+1)
        return include or exclude

a = Solution()

print(a.subset_sum([3, 34, 4, 12, 5, 2], 9))
print(a.subset_sum([1, 2, 3], 5))
print(a.subset_sum([1, 2, 3], 7))
print(a.subset_sum([2, 4, 6, 8], 10))
print(a.subset_sum([2, 4, 6, 8], 5))
print(a.subset_sum([5, 5, 5, 5], 10))
print(a.subset_sum([1, 1, 1, 1, 1], 3))
print(a.subset_sum([], 0))
print(a.subset_sum([10], 10))
print(a.subset_sum([10], 5))


