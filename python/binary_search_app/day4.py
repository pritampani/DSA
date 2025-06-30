# # return number of element perent in the array less than ot equal to x
# class Solution:
#     def binaryser(self,arr,x):
#         if len(arr)==0:
#             return -1
#         l=0
#         r=len(arr)-1
#         ans=-1
#         while l<=r:
#             mid=(l+r)//2
#             if arr[mid]<=x:
#                 ans=mid
#                 l=mid+1
#             else:
#                 r=mid-1
#         return ans+1

# a=Solution()
# print(a.binaryser([1,2,3,4,5,6,7],4))
# print(a.binaryser([1,2,3,4,5,6,7],4))
# print(a.binaryser([1,2,3,4,5,6,7],6))
# print(a.binaryser([1,2,3,4,5,6,7],7))
# print(a.binaryser([],4))





#81. Search in Rotated Sorted Array II\


# class Solution:
#     def search(self, arr: List[int], x: int) -> bool:
#         l=0
#         h=len(arr)-1
#         while l<=h:
#             mid=(l+h)//2
#             if arr[mid]==x:
#                 return True
#             if arr[l]==arr[mid]==arr[h]:
#                 l+=1
#                 h-=1
#                 continue
#             if arr[l]<=arr[mid]:
#                 if arr[l]<=x and x<arr[mid]:
#                     h=mid-1
#                 else:
#                     l=mid+1
#             else:

#                 if arr[mid]<x and x<=arr[h]:
#                     l=mid+1
#                 else:
#                     h=mid-1
#         return False
    

# a= Solution()
# print(a.search([1,2,3,4,5,55,666],2))


