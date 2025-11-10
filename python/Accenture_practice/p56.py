#Find rotation count in rotated array


class Solution:
    def rotation_count(self,arr):
        l=0
        r=len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]> arr[r]:
                l=mid+1
            else:
                r=mid
        return l

a = Solution()
print(a.rotation_count([5, 6, 7, 8, 9, 1, 2, 3, 4]))  # Output: 1
print(a.rotation_count([1, 2, 3, 4, 5]))              # Output: 1
print(a.rotation_count([3, 4, 5, 1, 2]))              # Output: 1
print(a.rotation_count([2, 1]))                       # Output: 1
print(a.rotation_count([1]))                          # Output: 1
print(a.rotation_count([3, 1, 2]))

