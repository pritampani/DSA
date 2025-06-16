#find min from sortd roatated array

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



#find max in the array

class Solution:
    def findmax(self,arr):
        l=0
        h=len(arr)-1
        ans=-1
        while l<=h:
            mid=(l+h)//2
            ans=max(arr[mid],ans)
            if arr[mid]<arr[l]:
                h=mid-1
            else:
                l=mid+1
        return ans

a=Solution()
    
print(a.findmax([5, 6, 7, 8, 9, 1, 2, 3, 4]))  # Output: 1
print(a.findmax([1, 2, 3, 4, 5]))              # Output: 1
print(a.findmax([3, 4, 5, 1, 2]))              # Output: 1
print(a.findmax([2, 1]))                       # Output: 1
print(a.findmax([1]))                          # Output: 1
print(a.findmax([3, 1, 2]))