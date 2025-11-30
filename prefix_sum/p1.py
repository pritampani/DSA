#1.	Running Sum of 1D Array

class Solution:
    def run_sum(self,arr):
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]+arr[i]
        return arr

a=Solution()
print(a.run_sum([1,2,3,4,5]))

