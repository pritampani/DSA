#     *
#    **
#   ***
#  ****
# *****




class Solution:
    def p1(self,n):
        for i in range(1,n+1):
            a=i-1
            print(' '*(n-i)+'*'*i) 

a=Solution()
a.p1(5)
