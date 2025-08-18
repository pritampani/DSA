#find min from sortd roatated array(Pritams approach)

# class Solution:
#     def findmin(self,arr):
#         l=0
#         h=len(arr)-1
#         ans=float('inf')
#         while l<=h:
#             mid=(l+h)//2
#             ans=min(arr[mid],ans)
#             if arr[mid]>arr[h]:
#                 l=mid+1
#             else:
#                 h=mid-1
#         return ans
# a = Solution()
# print(a.findmin([5, 6, 7, 8, 9, 1, 2, 3, 4]))  # Output: 1
# print(a.findmin([1, 2, 3, 4, 5]))              # Output: 1
# print(a.findmin([3, 4, 5, 1, 2]))              # Output: 1
# print(a.findmin([2, 1]))                       # Output: 1
# print(a.findmin([1]))                          # Output: 1
# print(a.findmin([3, 1, 2]))





class Solution:
    def findmin(self,arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            # If mid element is greater than the high element,
            # the minimum must be in the right half
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid  # Minimum is at mid or in the left half

        return arr[low]
a = Solution()
print(a.findmin([5, 6, 7, 8, 9, 1, 2, 3, 4]))  # Output: 1
print(a.findmin([1, 2, 3, 4, 5]))              # Output: 1
print(a.findmin([3, 4, 5, 1, 2]))              # Output: 1
print(a.findmin([2, 1]))                       # Output: 1
print(a.findmin([1]))                          # Output: 1
print(a.findmin([3, 1, 2]))

#find max in the array

# class Solution:
#     def findmax(self,arr):
#         l=0
#         h=len(arr)-1
#         ans=-1
#         while l<=h:
#             mid=(l+h)//2
#             ans=max(arr[mid],ans)
#             if arr[mid]<arr[l]:
#                 h=mid-1
#             else:
#                 l=mid+1
#         return ans

# a=Solution()
    
# print(a.findmax([5, 6, 7, 8, 9, 1, 2, 3, 4]))  # Output: 1
# print(a.findmax([1, 2, 3, 4, 5]))              # Output: 1
# print(a.findmax([3, 4, 5, 1, 2]))              # Output: 1
# print(a.findmax([2, 1]))                       # Output: 1
# print(a.findmax([1]))                          # Output: 1
# print(a.findmax([3, 1, 2]))




# Find a smallest divisor for a given threshold

# import math
# class Solution:
#     def smallestDivisor(self,arr,k):
#         return self.binarysearch(arr,k)

#     def binarysearch(self,arr,k):
#         l=1
#         h=max(arr)
#         ans=float('inf')
#         while l<=h:
#             mid=(l+h)//2
#             if self.ispossible(arr,k,mid):
#                 ans=min(ans,mid)
#                 h=mid-1
#             else:
#                 l=mid+1
#         return ans 
#     def ispossible(self,arr,k,mid):
#         sumo=0
#         for i in range(len(arr)):
#             sumo+=math.ceil(arr[i]/mid)
#         return sumo<=k
# a=Solution()
# print(a.smallestDivisor([1, 2, 5, 9],6))






        

