#4Sum problem==tar

class Solution:
    def four_sum(self,arr,tar):
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                newtar=tar-(arr[i]+arr[j])
                l=j+1
                r=len(arr)-1
                
                while l<r:
                    k=arr[l]+arr[r]
                    if k==newtar:
                        return True
                    if k>newtar:
                        r-=1
                    else:
                        l+=1
        return False
a = Solution()

print(a.four_sum([1, 0, -1, 0, -2, 2], 0))
print(a.four_sum([2, 3, 4, 5, 6], 50))
print(a.four_sum([-2, -1, 0, 1, 2, 3], 2))
print(a.four_sum([2, 2, 2, 2, 2], 8))
print(a.four_sum([1, 2, 3], 6))
print(a.four_sum([1, 0, -1, 0, -2, 2, 3, -3], 0))
print(a.four_sum([0, 0, 0, 0, 0], 0))



