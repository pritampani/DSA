# Search element in rotated sorted array


class Solution:
    def search_rotate(self,arr,tar):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==tar:
                return mid
            if arr[mid]>=arr[l]:
                if arr[l]<=tar<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<tar<=arr[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

a = Solution()
print(a.search_rotate([4,5,6,7,0,1,2], 0))  # Output: 4
print(a.search_rotate([4,5,6,7,0,1,2], 3))  # Output: -1