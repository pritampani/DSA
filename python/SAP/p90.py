# 5.	Find Second Largest Element in Array
# 	•	Without sorting the array.


class Solution:
    def second_largest(self,arr):

        m1 = float('-inf')
        m2 = float('-inf')
        for i in range(len(arr)):
            if arr[i]>m1:
                m2=m1
                m1=arr[i]
            elif arr[i]>m2 and arr[i]!=m1:
                m2=arr[i]

        return m2 if m2 != float('-inf') else None
    

a = Solution()
print(a.second_largest([10, 8, 6, 4]))     # 8
print(a.second_largest([10, 10, 5, 3]))    # 5
print(a.second_largest([-5, -2, -9]))      # -5
print(a.second_largest([1, 1, 1]))         # None
print(a.second_largest([7]))               # None