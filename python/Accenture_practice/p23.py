#Find second largest element


class Solution:
    def second_largest(self,arr):
        maxi=0
        secondmaxi=0
        for i in range(len(arr)):
            if arr[i]>maxi:
                secondmaxi=maxi
                maxi=arr[i]
        return secondmaxi

a=Solution()
print(a.second_largest([1,2,3,4,5,12,32]))