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
# class Solution:
#     def threesum(self,arr,target):
#         arr.sort()
#         i=0
#         if i==len(arr):
#             return False
#         return self.helper(arr,0,target)

#     def helper(self, arr,i, target):
#         if i>=len(arr)-2:
#             return False
#         if self.twosum(arr,i+1,len(arr)-1,target-arr[i]):
#             return True
#         return self.helper(arr,i+1,target)

#     def twosum(self, arr, l, h,target):
#         if l >= h:
#             return False  # Explicit False when no pair found
        
#         if arr[l] + arr[h] == target:
#             return True
#         elif arr[l] + arr[h] < target:
#             return self.twosum(arr, l + 1, h,target)
#         else:
#             return self.twosum(arr, l, h - 1,target)
            
# a=Solution()
# arr=[1,2,9,3,3,3,2,3,2,2,4,5,6,0,7,7,86,5,6,3,3,4,6,6]
# t=6
# print(a.threesum(arr,t))



#Qudrasum

# class Solution:
#     def qudrasum(self,arr,target):
#         arr.sort()
#         i=0
#         if i==len(arr):
#             return False
#         return self.helper(arr,0,target)

#     def helper(self, arr,i, target):
#         if i>=len(arr)-2:
#             return False
#         if self.twosum(arr,i+1,len(arr)-1,target-arr[i]):
#             return True
#         return self.helper(arr,i+1,target)

#     def twosum(self, arr, l, h,target):
#         if l >= h:
#             return False  # Explicit False when no pair found
        
#         if arr[l] + arr[h] == target:
#             return True
#         elif arr[l] + arr[h] < target:
#             return self.twosum(arr, l + 1, h,target)
#         else:
#             return self.twosum(arr, l, h - 1,target)
   
# a=Solution()
# arr=[1,2,9,3,3,3,2,3,2,2,4,5,6,0,7,7,86,5,6,3,3,4,6,6]
# t=6
# print(a.threesum(arr,t))



#qudra sum


class Solution:
    def qudra_sum(self,arr):
        if len(arr)<4:
            return 'arr len is less'
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                left=j+1
                right=len(arr)-1
                while left<right:
                    total=arr[i]+arr[j]+arr[left]+arr[right]
                    if total==0:
                        return True
                    if total>0:
                        right-=1
                    else:
                        left+=1
        return False

a=Solution()
#qudra sum


class Solution:
    def qudra_sum(self,arr):
        if len(arr)<4:
            return 'arr len is less'
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                left=j+1
                right=len(arr)-1
                while left<right:
                    total=arr[i]+arr[j]+arr[left]+arr[right]
                    if total==0:
                        return True
                    if total>0:
                        right-=1
                    else:
                        left+=1
        return False

a=Solution()
print(a.qudra_sum([1,2,-3,-5,4]))
print(a.qudra_sum([1,2,-3,-4,4,3]))
print(a.qudra_sum([-45,33,16,14,23,23,23,34,34,34,56,67,78,90]))
print(a.qudra_sum([1,2,-3,3,-6,6]))
print(a.qudra_sum([1,2,-3]))
print(a.qudra_sum([0,0,0,0]))



# class Solution:
#     def sum_k_element_equal_to_target(self,arr,k):

        
