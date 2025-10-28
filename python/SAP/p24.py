#Remove duplicates from sorted array


class Solution:
    def remove_duplicate(self,arr):
        if not arr:
            return 0
        
        j=0
        for i in range(1,len(arr)):
            if arr[i]!=arr[j]:
                j+=1
                arr[j]=arr[i]
        for i in range(j+1,len(arr)):
            arr[i]=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==0:
                arr.pop()
        return arr

a=Solution()
print(a.remove_duplicate([1,1,2,2,3,3,4,4,5]))

