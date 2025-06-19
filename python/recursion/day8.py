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