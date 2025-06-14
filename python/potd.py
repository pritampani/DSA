class Solution:
    def bs(self, arr, low, high, x):
        if arr[high] <= x:
            return high
        if arr[low] > x:
            return low
        
        mid = (low + high) // 2

        if arr[mid] <= x and arr[mid + 1] > x:
            return mid
        elif arr[mid] < x:
            return self.bs(arr, mid + 1, high, x)
        return self.bs(arr, low, mid - 1, x)



    def printKClosest(self, arr, n, k, x):
        id1 = self.bs(arr, 0, n - 1, x)
        
        id2 = id1 + 1

        if id1 >= 0 and arr[id1] == x:
            id1 -= 1
        
        ans = []
        for _ in range(k):

            if id1 >= 0 and id2 < n:
                val1 = x - arr[id1]
                val2 = arr[id2] - x

                if val1 < val2:
                    ans.append(arr[id1])
                    id1 -= 1
                else:
                    ans.append(arr[id2])
                    id2 += 1
            elif id1 >= 0:
                ans.append(arr[id1])
                id1 -= 1
            else:
                ans.append(arr[id2])
                id2 += 1
        
        return ans


a = Solution()
print(a.printKClosest([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56],13,4,35))