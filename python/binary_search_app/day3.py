class Solution:
    def sqt(self,n):
        l=1
        h=(n//2)//2
        ans=0
        while l<=h:
            mid=(l+h)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                l=mid+1
                ans=mid
                
            else:
                h=mid-1
        return ans
a=Solution()
print(a.sqt(30))