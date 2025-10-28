# Implement Selection Sort

class Solution:
    def selectionSort(self,arr):
        n=len(arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr

a=Solution()
print(a.selectionSort([3,6,2,1,6,1,8,4,5]))