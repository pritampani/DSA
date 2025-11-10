# 4.	Remove Duplicates from Sorted Array
# 	•	Modify array in-place and return new length.

class Solution:
    def remove_dup(self,arr):
        j=0
        for i in range(len(arr)):
            if arr[i]!=arr[j]:
                j+=1
                arr[j]=arr[i]
        return j+1
a = Solution()
arr = [1, 1, 2, 2, 3, 3, 3, 4]
new_len = a.remove_dup(arr)
print(new_len)     # 4
print(arr[:new_len])  # [1, 2, 3, 4]

