class Solution:
    def next_suprior_element_right(self,arr):

        c=1
        maxi=arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>maxi:
                c+=1
                maxi=arr[i]
        return c



