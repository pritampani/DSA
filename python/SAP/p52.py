#Allocate minimum pages (binary search on answer)



class Solution:
    def binary_serch(self, arr,k):
        n=len(arr)
        if n<k:
            return -1

        l=max(arr)
        r=sum(arr)
        while l<r:
            mid=(l+r)//2
            if self.ispossible(arr,k,mid):
                r=mid
            else:
                l=mid+1
        return l
    def ispossible(self,arr,k,maxpages):
        student=1
        currentpages=0
        for i in arr:
            if i + currentpages>maxpages:
                student+=1
                currentpages=i
                if student>k:
                    return False
            else:
                currentpages+=i
        return True

a=Solution()
print(a.binary_serch([12,23,34,45],2))
