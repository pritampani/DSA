#3.	Find Pivot Index


class Solution:
    def p3(self,arr):
        total=sum(arr)
        leftsum=0
        for i in range(len(arr)):
            
            if leftsum==total-leftsum-arr[i]:
                return i
            leftsum+=arr[i]
        return -1

a=Solution()
print(a.p3([1,7,3,6,5,6]))
