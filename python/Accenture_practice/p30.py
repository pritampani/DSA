#Implement Quick Sort

class Solution:
    def quickSort(self, arr):
        self._quickSort(arr, 0, len(arr) - 1)
        return arr

    def quickSort(self, arr, low, high):
        if low < high:
            
            pi = self.partition(arr, low, high)

           
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]  
        i = low - 1         

        for j in range(low, high):
            if arr[j] < pivot:     
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1



a = Solution()
print(a.quickSort([10, 7, 8, 9, 1, 5]))