#Intersection of two sorted arrays



class Solution:
    def intersection(self,a,b):
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                res.append(a[i]) #agar is me duplicate nai dal na he to check kar lena last entered element ye to nai kar ke 
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return res

a=Solution()
print(a.intersection([1,2,2,3,4,5],[2,2,5]))
print(a.intersection([1, 2, 4, 5, 6], [2, 3, 5, 7]))
 



