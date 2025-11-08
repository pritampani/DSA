#Merge Two Sorted Arrays


class Solution:
    def merge(self,a,b):
        i=0
        j=0
        arr=[]
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                arr.append(a[i])
                i+=1
            elif b[j]<a[i]:
                arr.append(b[j])
                j+=1
            else:
                arr.append(a[i])
                arr.append(b[j])
                i+=1
                j+=1
        while i<len(a):
            arr.append(a[i])
            i+=1
        while j<len(b):
            arr.append(b[j])
            j+=1
        return arr

a = Solution()

print(a.merge([1,3,5], [2,4,6]))         # [1,2,3,4,5,6]
print(a.merge([1,2,3], [2,3,4]))         # [1,2,2,3,3,4]
print(a.merge([], [1,2,3]))              # [1,2,3]
print(a.merge([1,2,3], []))              # [1,2,3]
print(a.merge([1,3,5], [1,3,5]))         # [1,1,3,3,5,5]



