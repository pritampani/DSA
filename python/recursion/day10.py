class Solution:
    def  towerOfHanoi(self, n, A,C,B):
        # code here
        if n==0:
            return 0
        res=self.towerOfHanoi(n-1,A,B,C)
        print(f"move {n} th Disk from {A} to {C}")
        res+=1
        res+=self.towerOfHanoi(n-1,B,C,A)
        return res

a=Solution()
print(a.towerOfHanoi(3,"A","C","B"))