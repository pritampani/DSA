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







def fun(stk):
    i=0
    return hlper(stk,i)

def hlper(stk,i):
    #base??
    if i==len(stk):
        return 0

    hlper(stk,i+1)
    print(stk[i])


#main
stk=[1,2,3,4,5]
fun(stk)



