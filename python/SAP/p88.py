# 3.	Move All Zeroes to End
# 	•	Maintain relative order.
# 	•	Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

class Solution:
    def move_zero(self,arr):
        pos=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[pos]=arr[pos],arr[i]
                pos+=1
        return arr

a = Solution()
print(a.move_zero([2, 1, 0, 3, 12,0,0,0,2]))