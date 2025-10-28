#Move all zeros to end


class Solution:
    def moveallzero(self,arr):

        j=0
        for i in range(len(arr)):
            if arr[i]!=0:
                
                arr[j]=arr[i]
                j+=1
        for k in range(j,len(arr)):
            arr[k]=0
        return arr

a=Solution()
print(a.moveallzero([1,2,3,0,3,0,2,0,5,0]))
            
        