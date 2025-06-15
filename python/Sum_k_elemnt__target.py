#Two Sum - Pair with Given Sum

# class Solution:
#     def twoSum(self, arr, target):
#         arr.sort()  # Important: sort the array first
#         l = 0
#         h = len(arr) - 1
#         return self.rec(arr, target, l, h)

#     def rec(self, arr, target, l, h):
#         if l >= h:
#             return False  # Explicit False when no pair found
        
#         if arr[l] + arr[h] == target:
#             return True
#         elif arr[l] + arr[h] < target:
#             return self.rec(arr, target, l + 1, h)
#         else:
#             return self.rec(arr, target, l, h - 1)
            
# a=Solution()
# arr=[1,2,9,3,3,3,2,3,2,2,4,5,6,0,7,7,86,5,6,3,3,4,6,6]
# t=16
# print(a.twoSum(arr,t))

#3sum(triplet sum)
class Solution:
    def threesum(self,arr,target):
        arr.sort()
        i=0
        if i==len(arr):
            return False
        return self.helper(arr,0,target)

    def helper(self, arr,i, target):
        if i>=len(arr)-2:
            return False
        if self.twosum(arr,i+1,len(arr)-1,target-arr[i]):
            return True
        return self.helper(arr,i+1,target)

    def twosum(self, arr, l, h,target):
        if l >= h:
            return False  # Explicit False when no pair found
        
        if arr[l] + arr[h] == target:
            return True
        elif arr[l] + arr[h] < target:
            return self.twosum(arr, l + 1, h,target)
        else:
            return self.twosum(arr, l, h - 1,target)
            
a=Solution()
arr=[1,2,9,3,3,3,2,3,2,2,4,5,6,0,7,7,86,5,6,3,3,4,6,6]
t=6
print(a.threesum(arr,t))

