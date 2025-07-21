# # * # % @
# class Solution:
#     def prossedstring(self, s):
#         stk = []
#         res = ""
        
#         for ch in s:
#             if ch == "*":
#                 stk += stk[:]  
#             elif ch == "#":
#                 if stk:
#                     stk.pop()
#             elif ch == "%":
#                 stk = stk[::-1]
#             elif ch == "@":
#                 res += ''.join(stk[i] for i in range(0, len(stk), 2))
#             else:
#                 stk.append(ch)
                
#         if res=="":
#             res+=''.join(stk)

#         return res


# #main

# a=Solution()

# print(a.prossedstring("a*b#cc"))
# print(a.prossedstring("abc@a#vc#abcde@*"))



