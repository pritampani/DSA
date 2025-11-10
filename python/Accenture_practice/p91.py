# 6.	Rotate Array by K Positions (Right Rotation)
# 	•	Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]


class Solution:
    def right_rotation(self,arr,k):
        k=k%len(arr)
        return arr[-k:]+arr[:-k]
a = Solution()
print(a.right_rotation([1, 2, 3, 4, 5], 2))