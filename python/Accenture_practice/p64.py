#3Sum problem==0

class Solution:
    def three_sum(self,arr):
        arr.sort()
        for i in range(len(arr)):
            l=i+1
            r=len(arr)-1
            while l<r:
                k=arr[i]+arr[l]+arr[r]
                if k==0:
                    return True
                elif k>0:
                    r-=1
                else:
                    l+=1
        return False


a = Solution()
print(a.three_sum([-1, 0, -1, -4]))

print(a.three_sum([-1, 0, 1, 2, -1, -4]))