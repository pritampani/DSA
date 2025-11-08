#Tower of Hanoi


class Solution:
    def tower_of_hanoi(self,n,A,B,C):
        if n==0:
            return 0
        
        r=self.tower_of_hanoi(n-1,A,C,B)
        
        l=self.tower_of_hanoi(n-1,B,A,C)
        return l+1+r

a = Solution()
print(a.tower_of_hanoi(3, 'A', 'B', 'C'))