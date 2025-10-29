	# 1.	Find Missing Number in Range 1…N
	# •	Example: [1, 2, 4, 5] → 3
	# •	Use sum formula or XOR approach.

class Solution:
    def missing_using_xor(self,arr):
        n=len(arr)+1

        xor_all=0
        xor_arr=0
        for i in range(1,n+1):
            xor_all^=i
        for num in arr:
            xor_arr^=num
        return xor_arr^xor_all

a = Solution()
print(a.missing_using_xor([1, 2, 4, 5]))     # 3
print(a.missing_using_xor([2, 3, 1, 5]))     # 4
print(a.missing_using_xor([1]))              # 2
print(a.missing_using_xor([2]))              # 1
print(a.missing_using_xor([1, 2, 3, 4, 6]))  # 5
