#Rotate array by k positions


class Solution:
    def rotatekpos(self,arr,pos):
        a=arr[:pos]
        b=arr[pos:]
        return b+a

a=Solution()
print(a.rotatekpos([1,2,3,4,5,6],4))