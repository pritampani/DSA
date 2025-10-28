#Find largest and smallest element



class Solution:
    def max_min(self,arr):
        mini=float('inf')
        maxi=float('-inf')

        for i in range(len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
            if arr[i]<mini:
                mini=arr[i]
        return mini,maxi

a=Solution()
print(a.max_min([1,2,3,4,5,56,6]))
                

