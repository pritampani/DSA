class Solution:
    def rowWithMax1s(self, arr):
        # code here
        maxi=0
        for i in range(len(arr)):
            c=0
            for j in range(len(arr[0])-1,-1,-1):
                if arr[i][j]==1:
                    c+=1
            maxi=max(maxi,c)
        return maxi



                
                

a=Solution()
arr=[[0,1,1,1], 
 [0,0,1,1], 
 [1,1,1,1],
 [0,0,0,0]]
print(a.rowWithMax1s(arr))