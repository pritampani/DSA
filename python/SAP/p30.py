#Implement Quick Sort

class Solution:
    def quickSort(self, arr):
        self._quickSort(arr, 0, len(arr) - 1)
        return arr

    def _quickSort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pi = self.partition(arr, low, high)

            # Recursively sort elements before and after partition
            self._quickSort(arr, low, pi - 1)
            self._quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]   # Choose the last element as pivot
        i = low - 1         # Index of smaller element

        for j in range(low, high):
            if arr[j] < pivot:      # If current element < pivot
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in the correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# Example usage
a = Solution()
print(a.quickSort([10, 7, 8, 9, 1, 5]))