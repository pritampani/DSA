#Next element with greater frequency

from collections import Counter
class Solution:
    def findGreater(self, arr):
        # code here
        freq=Counter(arr)
        stk=[]
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            while stk and freq[stk[-1]]<=freq[arr[i]]:
                stk.pop()
            if not stk:
                ans.append(-1)
            else:
                ans.append(stk[-1])
            stk.append(arr[i])

        return ans[::-1]


a=Solution()
print(a.findGreater([2, 1, 1, 3, 2, 1]))