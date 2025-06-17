# decerive a recursive function for converting the string to integer


# class Solution:
#     def strtoint(self,s):
#         i=0
#         n=len(s)
#         res=0
#         return self.helper(s,i,n,res)
#     def helper(self,s,i,n,res):
#         if i==n:
#             return res
#         return self.helper(s,i+1,n,(res*10)+int(s[i]))


# a=Solution()
# b='1234'
# print(type(a.strtoint(b)))



#c4.9 write a short recursivve python function that finds the minimum and the maximum  values in from a array without using of loop

# class Solution:
#     def maxminval(self,arr):
#         if len(arr)==0:
#             return ()
#         i=0
#         n=len(arr)
#         val1=arr[0]
#         val2=arr[0]
#         return self.maxval(arr,i,n,val1),self.minval(arr,i,n,val2)
#     def maxval(self,arr,i,n,val):
#         if i==n:
#             return val
#         return self.maxval(arr,i+1,n,max(val,arr[i]))
#     def minval(self,arr,i,n,val):
#         if i==n:
#             return val
#         return self.minval(arr,i+1,n,min(val,arr[i]))
    
# a=Solution()
# print(a.maxminval([1,2,3,4,5,6,7,8]))
# print(a.maxminval([1, 2, 3, 4, 5, 6, 7, 8]))   # (8,1)
# print(a.maxminval([-5, -3, -10]))              # (-3,-10)
# print(a.maxminval([7]))                        # (7,7)
# print(a.maxminval([])) 




#4.12 computer the product of m*n using only addition and substraction

# class Solution:
#     def productmn(self, m, n):
#         if m == 0 or n == 0:
#             return 0
#         if n < 0:
#             # Convert to positive and negate result
#             return -self.productmn(m, -n)
#         return self.helper(m, n, 0)

#     def helper(self, m, n, pro):
#         if n == 0:
#             return pro
#         return self.helper(m, n - 1, pro + m)

# a = Solution()
# print(a.productmn(2, 4))     # 8
# print(a.productmn(-2, 4))    # -8
# print(a.productmn(2, -4))    # -8
# print(a.productmn(-2, -4))   # 8
# print(a.productmn(0, 5))     # 0
# print(a.productmn(5, 0))     # 0 




#Tower of Hanoi

class Solution:
    def towerhanoi(self, n, A="A", B="B", C="C"):
        return self.helper(n, A, B, C)

    def helper(self, n, source, auxiliary, target):
        if n == 1:
            # Move 1 disk from source to target
            return 1
        # Move n-1 disks from source to auxiliary using target as buffer
        res = self.helper(n - 1, source, target, auxiliary)
        # Move 1 disk from source to target
        res += 1
        # Move n-1 disks from auxiliary to target using source as buffer
        res += self.helper(n - 1, auxiliary, source, target)
        return res

a = Solution()
print(a.towerhanoi(3))  

