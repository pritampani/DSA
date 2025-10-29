# Aggressive cows problem


class Solution:
    def binary_search(self,arr,k):
        arr.sort()
        l=1
        r=sum(arr)
        ans=-1

        while l<=r:
            mid=(l+r)//2
            if self.can_palce(arr,k,mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans

    def can_palce(self,stalls,k,dist):
        count=1
        last_pos=stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i]-last_pos>=dist:
                count+=1
                last_pos=stalls[i]
                if count==k:
                    return True
        return False


# Example Usage
a = Solution()
print(a.binary_search([1, 2, 8, 4, 9], 3))  # ✅ Output: 3
