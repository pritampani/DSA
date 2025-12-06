#check the array is sorted or not?? using recursion



# class Solution:
#     def issorted(self,arr,n):
#         if n==0:
#             return True
#         return self.helper(arr,n,0)
#     def helper(self,arr,n,i):
#         if i==len(arr)-1:
#             return True
        
#         if arr[i]>arr[i+1]:
#             return False
        
#         else:
#             remaningpart=self.helper(arr,n-1,i+1)
#             return remaningpart

# a=Solution()
# print(a.issorted([1,2,3,4,5],5))   # True
# print(a.issorted([1,2,3,9,5],5))   # False
# print(a.issorted([],0))            



#reverse a string using recursion


# class Solution:
#     def reversestr(self,s)->str:
#         return self.helper(s,len(s)-1)
#     def helper(self,s,n):

#         if n==0:
#             return s[n]
#         return s[n]+self.helper(s,n-1)

# a=Solution()
# print(a.reversestr('abcd'))
# print(a.reversestr('chiku'))




#check for plandrom for of a string in recursive way


class Solution:
    def check_palandrom(self,s)->bool:
        return self.helper(s,0,len(s)-1)
    
    def helper(self,s,i,j):
        if s[i]!=s[j]:
            return False
        if i>=j:
            return True
        return self.helper(s,i+1,j-1)


a=Solution()
print(a.check_palandrom('abcba'))
print(a.check_palandrom('chiku'))
print(a.check_palandrom('ab'))