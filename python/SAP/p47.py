#Find peak element


class Solution:
    def peak_element(self,arr):
        l=0
        r=len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]<arr[mid+1]:
                l+=1
            else:
                r=mid
        return l

a = Solution()
print(a.peak_element([1, 2, 3, 1]))            # Output: 2
print(a.peak_element([1, 2, 1, 3, 5, 6, 4]))   # Output: 5 or 1