#Minimum difference element in sorted array
# arr = [1, 3, 8, 10, 15]
# x = 9
# Between 8 and 10:
# 	•	|9 - 8| = 1
# 	•	|10 - 9| = 1

# ✅ Either 8 or 10 is fine. Usually, we return the smaller one → 8.


class Solution:
    def binary_search(self,arr,x):
        l=0
        r=len(arr)-1
        if x<=arr[0]:
            return arr[0]
        if x>=arr[-1]:
            return arr[-1]
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==x:
                return arr[mid]
            if arr[mid]<x:
                l=mid+1
            else:
                r=mid-1
        if l<len(arr) and r>=0:
            if abs(arr[l]-x)<abs(arr[r]-x):
                return arr[l]
            else:
                return arr[r]
            
            
a = Solution()
print(a.binary_search([1, 3, 8, 10, 15], 12))  # ✅ Output: 10
print(a.binary_search([2, 5, 6, 7, 8, 8, 9], 4))  # ✅ Output: 5
print(a.binary_search([1, 3, 8, 10, 15], 9))   # ✅ Output: 8
print(a.binary_search([1, 3, 8, 10, 15], 2))   # ✅ Output: 1
print(a.binary_search([1, 3, 8, 10, 15], 16))  # ✅ Output: 15
