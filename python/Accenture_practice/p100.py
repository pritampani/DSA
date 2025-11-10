# 🔢 Problem: Product of Array Except Self

# 🧩 Problem Statement

# Given an integer array nums, return an array output where
# output[i] = product of all elements of nums except nums[i].

# ⚠️ You must not use division, and your algorithm should run in O(n) time.

# ⸻

# Example
# Input:  nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]


class Solution:
    def product_arr_expect_itself(self,arr):
        c=0
        pro=1
        for i in range(len(arr)):
            if arr[i]==0:
                c+=1
            else:
                pro*=arr[i]
        if c>=2:
            return [0]*len(arr)
        if c==1:
            res=[0]*len(arr)
            for i in range(len(arr)):
                if arr[i]==0:
                    res[i]=pro
                    return res
        else:
            res=[0]*len(arr)
            for i in range(len(arr)):
                res[i]=pro//arr[i]
            return res
    def non_devision_prefix_sum_trick(self,arr):
        n=len(arr)
        res=[1]*n
        left=1
        for i in range(n):
            res[i]=left
            left*=arr[i]
        right=1
        for i in range(n-1,-1,-1):
            res[i]*=right
            right*=arr[i]
        return res

a = Solution()
# print(a.product_arr_expect_itself([1, 2, 3, 4]))  # ✅ [24, 12, 8, 6]
# print(a.product_arr_expect_itself([0, 2, 3, 4]))  # ✅ [24, 0, 0, 0]
# print(a.product_arr_expect_itself([0, 2, 0, 4]))  # ✅ [0, 0, 0, 0]
print(a.non_devision_prefix_sum_trick([1, 2, 3, 4]))  # ✅ [24, 12, 8, 6]
print(a.non_devision_prefix_sum_trick([0, 2, 3, 4]))  # ✅ [24, 0, 0, 0]
print(a.non_devision_prefix_sum_trick([0, 2, 0, 4]))  # ✅ [0, 0, 0, 0]


