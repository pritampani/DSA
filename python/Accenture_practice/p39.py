#Majority element


class Solution:
    def majority(self,arr):
        candi=0
        count=0
        for i in range(len(arr)):
            if count<=0:
                candi=arr[i]
                count=1
            elif candi==arr[i]:
                count+=1
            else:
                count-=1
        
        vote = arr.count(candi)
        if vote > len(arr) // 2:
            return candi
        return -1  

a=Solution()
print(a.majority([1,1,2,3,3,4,4,4,5,5,5,66,6,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
