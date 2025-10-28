#Move negative numbers to one side


class Solution:
    def move_negative(self,arr):
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l]<0 and arr[r]>0:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            elif arr[l]>0:
                l+=1
            else:
                r-=1
        return arr

a = Solution()
print(a.move_negative([-1, -2, 3, -4, 5, 6]))