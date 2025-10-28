# Reverse an array


class Solution:
    def reverse_array(self,arr):
        l=0
        r=len(arr)-1

        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
        return arr

a=Solution()
print(a.reverse_array([1,2,3,4,56,67,7]))