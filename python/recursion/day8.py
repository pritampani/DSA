# # wite a recursive function that reverse the string

# class Solution:
#     def reverse(self,s):
#         if s=='':
#             return s
#         i=len(s)-1
#         res=''
#         return self.helper(s,i,res)

#     def helper(self,s,i,res):
#         if i==-1:
#             return res
#         return self.helper(s,i-1,res+s[i])
# a=Solution()
# print(a.reverse('chiku'))

#O(n) time and space efficient.
# class Solution:
#     def reverse(self, s):
#         if s == '':
#             return s
#         res = []
#         self.helper(s, len(s) - 1, res)
#         return ''.join(res)

#     def helper(self, s, i, res):
#         if i == -1:
#             return
#         res.append(s[i])
#         self.helper(s, i - 1, res)

# a = Solution()
# print(a.reverse('chiku'))  # Output: 'ukihc'



# check if the string is palandrom or not

# class Solution:
#     def check_reverse(self,s):
#         if s=='':
#             return True
#         i=len(s)-1
#         res=''
#         res=self.helper(s,i,res)
#         return s==res
#     def helper(self,s,i,res):
#         if i==-1:
#             return res
#         res+=s[i]
#         return self.helper(s,i-1,res)
# a=Solution()
# print(a.check_reverse('abba'))
# print(a.check_reverse('chiku'))
# print(a.check_reverse(''))






#write a python function which can show how many vowels and consonant are there in a string

# class Solution:
#     def countvowleandconsonant(self,s):
#         if s=='':
#             return (0,0)
#         i=len(s)-1
#         v=0
#         c=0
#         return self.helper(s,i,v,c)
#     def helper(self,s,i,v,c):
#         if i==-1:
#             return v,c
#         if s[i] in ('a','e','i','o','u','A','E','I','O','U'):
#             return self.helper(s,i-1,v+1,c)
#         elif s[i].isalpha():
#             return self.helper(s,i-1,v,c+1)
#         else:
#             return self.helper(s,i-1,v,c)

# a = Solution()
# print(a.countvowleandconsonant('aeiouqwrt'))  # (5,4)
# print(a.countvowleandconsonant('123'))        # (0,0)
# print(a.countvowleandconsonant('hello!'))     # (2,3)
# print(a.countvowleandconsonant(' hi '))       # (1,1)
# print(a.countvowleandconsonant('')) 




# write a python function so that it will rearrange all the even value 

# class Solution:
#     def rearrange(self,arr):
#         if len(arr)<=1:
#             return []
#         i=0
#         j=len(arr)-1
#         return self.helper(arr,i,j)
#     def helper(self,arr,i,j):
#         if i>=j:
#             return arr
#         if arr[j]%2==0 and arr[i]%2!=0:
#             arr[j],arr[i]=arr[i],arr[j]
#             return self.helper(arr,i+1,j-1)
#         else:
#             return self.helper(arr,i+1,j-1)
# a=Solution()
# print(a.rearrange([1,9,2,8,3,7,4,6,5]))




