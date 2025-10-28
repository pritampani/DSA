#Number pyramid


class Solution:
    def num_primyed(self,n):
        for i in range(1,n):
            print(" "*(n-i),end=' ')

            for j in range(1,i+1):
                print(j,end="")
            for j in range(i-1,0,-1):
                print(j,end="")
            print()
a=Solution()
a.num_primyed(7)

