#Find intersection of two arrays
# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 3, 5]
# Elements that appear in both arrays
# → [2, 2, 3]
class Solution:
    def intersection(self,arr1,arr2):
        a=set(arr1)
        res=[]
        for i in arr2:
            if i in a:
                res.append(i)
        return -1 if len(res)==0 else res

a=Solution()
print(a.intersection([1,2,4,5,6],[1,2,6,7,8,90]))

