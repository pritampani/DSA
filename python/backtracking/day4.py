# All Palindromic Partitions


# class Solution:
#     def palinParts(self, s):
#         res = []
#         self.helper(s, 0, [], res)
#         return res

#     def helper(self, s, start, curr, res):
#         if start == len(s):
#             res.append(curr[:])
#             return

#         for end in range(start + 1, len(s) + 1):
#             substr = s[start:end]
#             if substr == substr[::-1]:  
#                 curr.append(substr)
#                 self.helper(s, end, curr, res)
#                 curr.pop()

# a=Solution()
# print(a.palinParts("geeks"))
# print(a.palinParts("abcba"))
# print(a.palinParts("aha"))

