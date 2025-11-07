#previous greater elemnet



class Solution:
    def PGE(self,arr):
        stk=[]
        res=[-1]*len(arr)
        for i in range(len(arr)):
            while stk and stk[-1]<=arr[i]:
                stk.pop()
            if stk:
                res[i]=stk[-1]
            stk.append(arr[i])
        return res


s = Solution()
print(s.PGE([3, 4, 2, 7, 5, 8, 10, 6]))   
print(s.PGE([1, 2, 3]))                  
print(s.PGE([5, 4, 3, 2]))               
print(s.PGE([10]))                       
print(s.PGE([]))                         
