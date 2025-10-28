"""
   *
  ***
 *****
*******

"""

class Solution:
    def pyramid(self,n):
        for i in range(1,n+1):
            print(' ' * (n - i) + '*' * (2*i-1))

a=Solution()
print(a.pyramid(4))
