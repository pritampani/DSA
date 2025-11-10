# .	Find Pivot Index (Equilibrium Point)

# 	•	Sum of elements on left = right.
# 	•	Example: [1,7,3,6,5,6] → index 3



class Solution:
    def epoint(self,arr):
        total_sum=sum(arr)
        ls=0
        for i in range(len(arr)):
            rs=total_sum-ls-arr[i]
            if ls==rs:
                return i
            ls+=arr[i]
        return -1
a = Solution()
print(a.pivot_index([1, 7, 3, 6, 5, 6]))   # 3
print(a.pivot_index([1, 2, 3]))            # -1
print(a.pivot_index([2, 1, -1]))           # 0
print(a.pivot_index([0, 0, 0, 0]))         # 0
print(a.pivot_index([1, -1, 1, -1, 1, -1])) # -1