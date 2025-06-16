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





#compute power a**b

# class Solution:
#     def powr(self,a,b):
#         if b==0:
#             return 1
#         c=1
#         i=0
#         return self.helper(a,b,i,c)
#     def helper(self,a,b,i,c):
#         if i==b:
#             return c
#         return self.helper(a,b,i+1,c*a)
# a=Solution()
# print(a.powr(2,3))


class Solution():
    def reversearr(self,arr):
        if not arr:
            return arr
        i=0
        j=len(arr)-1
        return self.helper(arr,i,j)

    def helper(self,arr,i,j):
        if i>j:
            return arr
        arr[i],arr[j]=arr[j],arr[i]
        return self.helper(arr,i+1,j-1)

a=Solution()
print(a.reversearr([1,2,3,4,5,6,7]))
print(a.reversearr([1,2,3,4,5,6]))



