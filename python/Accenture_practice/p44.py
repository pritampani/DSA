#Find leaders in array

# arr = [16, 17, 4, 3, 5, 2]
# ✅ Leaders = [17, 5, 2]

# (Usually printed in order of appearance → [17, 5, 2])




class Solution:
    def leader(self,arr):
        res=[]
        current=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>current:
                res.append(arr[i])
                current=arr[i]
        return res[::-1]

a=Solution()
print(a.leader([16, 17, 4, 3, 5, 2]))