#Find all pairs with difference k


class Solution:
    def find_pair(self,arr,k):
        arr.sort()
        l=0
        r=1
        res=[]
        while r<len(arr):
            diff=arr[r]-arr[l]
            if diff==k:
                res.append((arr[l],arr[r]))
                l+=1
                r+=1
            elif diff<k:
                r+=1
            else:
                l+=1
                if l==r:
                    r+=1
        return res

a = Solution()
print(a.find_pair([1, 5, 3, 4, 2], 2))
