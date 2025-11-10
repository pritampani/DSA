#Sort 0s, 1s, 2s (Dutch National Flag)


class Solution:
    def Dutch_National_flag(self,arr):
        l=0
        mid=0
        r=len(arr)-1
        while mid<=r:
            if arr[mid]==0:
                arr[l],arr[mid]=arr[mid],arr[l]
                l+=1
                mid+=1
            elif arr[mid]==2:
                arr[mid],arr[r]=arr[r],arr[mid]
                r-=1
            else:
                mid+=1
        return arr
a=Solution()
print(a.Dutch_National_flag([2,2,2,1,1,1,0,0,0]))
            