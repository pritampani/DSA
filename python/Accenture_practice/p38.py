#Find duplicate element in array

class Solution:
    def findduplicate(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return num
            seen.add(num)
        return -1

a = Solution()
print(a.findduplicate([1,-49,2,4,49]))




