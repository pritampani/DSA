class Solution:
    def generate_subarray(self,arr):
        res=[]
        stk=[]
        i=0
        self.helper(arr,i,stk,res)
        return res
    def helper(self,arr,i,stk,res):
        # base case"??
        if i==len(arr):
            res.append(stk[:])
            return 0


        stk.append(arr[i])
        self.helper(arr,i+1,stk,res)

        stk.pop()

a=Solution()
print(a.generate_subarray([1,2,3]))



