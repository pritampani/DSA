#Implement Bubble Sort

class Solution:
    def bubble_sort(self,arr):
        n=len(arr)
        for i in range(n-1):
            swap=False
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swap=True
            if not swap:
                break
        return arr

a=Solution()
print(a.bubble_sort([3,6,2,1,6,1,8,4,5]))
        








