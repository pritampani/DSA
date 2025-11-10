#Find subarray with given sum (positive numbers)



class Solution:
    def subarraySum(self,arr,t):
        i=0
        c=0
        for j in range(len(arr)):
            c+=arr[j]
            while c>t and i<=j:
                c-=arr[i]
                i+=1
            if c==t:
                return [i+1,j+1]
        return [-1]

a = Solution()

print(a.subarraySum([1, 2, 3, 7, 5], 12))
print(a.subarraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
print(a.subarraySum([5, 3, 4], 2))
print(a.subarraySum([10, 20, 30], 20))
print(a.subarraySum([2, 4, 6, 8], 20))
print(a.subarraySum([1, 1, 1, 2, 3], 3))
print(a.subarraySum([4, 5, 6], 2))
print(a.subarraySum([2]*10, 8))
print(a.subarraySum([1, 2, 3, 4], 0))
print(a.subarraySum([5], 10))





