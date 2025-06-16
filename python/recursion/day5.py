# class Solution:
#     def fibbo(self,n):
#         if n<=1:
#             return n
#         return self.fibbo(n-1)+self.fibbo(n-2)
# a=Solution()
# print(a.fibbo(10))





# class Solutin:
#     def print1ton(self,n,i):
#         if i==n:
#             return i
#         print(i)
#         return self.print1ton(n,i+1)
# a=Solutin()
# print(a.print1ton(10,0))




 #describe a recursive algo for finding the max element from array

# class Solution:
#     def maxele(self,arr,n):
#         if n==0:
#             return 0
#         maxi=arr[0]
#         i=0
#         return self.helper(arr,i,n,maxi)

#     def helper(self,arr,i,n,maxi):
#         if i==n:
#             return maxi
#         return self.helper(arr,i+1,n,max(maxi,arr[i]))
# a=Solution()
# arr=[]
# n=len(arr)
# print(a.maxele(arr,n))





#compute power

class Solution:
    