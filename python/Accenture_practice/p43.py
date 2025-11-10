#Kadane’s algorithm (maximum subarray sum)



class Solution:

    def kad(self,arr):
        maxi=arr[0]
        cs=0
        for i in range(len(arr)):
            cs+=arr[i]
            maxi=max(cs,maxi)
            if cs<=0:
                cs=0
        return maxi


a=Solution()
print(a.kad([1,2,3,4,66,7,8]))
print(a.kad([1, 1, 1, 1]))

