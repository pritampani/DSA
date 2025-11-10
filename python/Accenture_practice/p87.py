# 2.	Find Element Appearing Once
# 	•	All numbers appear twice except one.
# 	•	Example: [2, 3, 2, 4, 4] → 3

class Solution:
    def apper_onse(self,arr):
        s=0
        for i in arr:
            s^=i
        return s
a = Solution()
print(a.apper_onse([2, 3, 2, 4, 4]))     # 3
print(a.apper_onse([5, 1, 1, 2, 2]))     # 5
print(a.apper_onse([10, 10, 99]))        # 99
print(a.apper_onse([7]))                 # 7
print(a.apper_onse([8, 3, 8, 5, 5]))     # 3
