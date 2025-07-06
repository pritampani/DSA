


# Max histogram area

class Solution:
    def next_smaller_elemnt(self,arr):
        stk=[]
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            while stk and arr[stk[-1]]>=arr[i]:
                stk.pop()
            if not stk:
                ans.append(len(arr))
            else:
                ans.append(stk[-1])
            stk.append(i)

        return ans[::-1]
    def previoussmallerelement(self,arr):
        stk=[]
        ans=[]
        for i in range(len(arr)):
            while stk and arr[stk[-1]]>=arr[i]:
                stk.pop()
            if not stk:
                ans.append(-1)
            else:
                ans.append(stk[-1])
            stk.append(i)

        return ans
    def Max_histogram_area(self,arr):

        a=self.next_smaller_elemnt(arr)
        b=self.previoussmallerelement(arr)
        maxi=0
        for i in range(len(arr)):
            width=(a[i]-b[i])-1
            maxi=max(maxi,width*arr[i])
        return maxi

a=Solution()
print(a.Max_histogram_area([6,2,5,4,5,1,6]))