#[ ] 25. Find the intersection of two arrays while preserving duplicate counts. Solve the basic version.



class Solution:
    def intersection(self,arr1,arr2):
        d={}
        
        for i in arr1:
            d[i]=d.get(i,0)+1
        a=d.copy()
        for j in arr2:
            if j in d:
                d[j]-=1
        
        res=[]
        for i in d:

            if d[i]==0:
                res+=([i] * a[i])
        return res

a=Solution()
arr1=[1,2,2,4,4,5,6]
arr2=[3,2,4,2,4,9]
print(a.intersection(arr1,arr2))
