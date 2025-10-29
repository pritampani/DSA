#Next greater element

class Solution:
    def NGE(self,arr):
        res=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            stack.append(arr[i])
        return res

a = Solution()
print(a.NGE([4, 5, 2, 25]))
print(a.NGE([13, 7, 6, 12]))
print(a.NGE([1, 3, 2, 4]))