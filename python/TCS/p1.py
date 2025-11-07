#1.Push Zeros to End


class Solution:
    def p1(self, arr):
        pos = 0  # position to place the next non-zero
        
        # Move all non-zeros to the front
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Fill remaining positions with zeros
        while pos < len(arr):
            arr[pos] = 0
            pos += 1
        
        return arr
# Testing your function
s = Solution()
arr=[-1, -1, 0, 0, 1, 2, 2]
print(s.p1(arr))