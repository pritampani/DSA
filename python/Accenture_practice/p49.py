#Find square root using binary search


class Solution:
    def find_sqrt(self,n):
        l=1
        r=n//2
        while l<=r:
            mid=(l+r)//2
            if (mid*mid)==n:
                return mid
            elif mid*mid>n:
                r=mid-1
            else:
                l=mid+1
        return -1

a=Solution()
print(a.find_sqrt(16))
print(a.find_sqrt(18))