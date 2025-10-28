"""
   *
  ***
 *****
*******


    1
   121
  12321
 1234321

"""

class Solution:
    def pyramid(self,n):
        for i in range(1,n+1):
            print(' ' * (n - i) + '*' * (2*i-1))
    def number_primyied(self,n):
        for i in range(1,n):
            for j in range(1,n):
                print(j,end=' ')
    def square(self,n):
        for i in range(n):
            print("*"*n)
    def triangle(self,n):
        for i in range(1,n):
            print(i*'*')
    def inv_triangle(self,n):
        for i in range(n-2,-1,-1):
            print(i*'*')
    def number_triangle(self,n):
        for i in range(1,n+1):
            for j in range(1,i):
                print(j,end=' ')
            print()
    def inv_number_triangle(self,n):
        for i in range(n-1,-1,-1):
            for j in range(i-1,0,-1):
                print(j,end=' ')
            print()

a=Solution()
#print(a.pyramid(4))
#print(a.number_primyied(4))
#print(a.square(5))
#print(a.triangle(4))
#print(a.inv_triangle(6))
#print(a.number_triangle(6))
#print(a.inv_number_triangle(8))

