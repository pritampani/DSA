#2.	Subarray Sum Equals K (count)


class Solution:
    def p2(self,arr,k):
        
        fre={0:1}
        prefix_sum=0
        count=0

        for x in arr:
            prefix_sum+=x
            if prefix_sum-k in fre:
                count+=fre[prefix_sum-k]
            fre[prefix_sum]=fre.get(prefix_sum,0)+1
        return count,fre


a=Solution()

nums = [10,20,10,20,10]
k = 30
print(a.p2(nums,k))



