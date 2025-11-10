#Rotate Matrix by 90 Degrees


class Solution:
    def rotate_matrix(self,arr):
        for i in range(len(arr)):
            for j in range(i,len(arr[0])):
                arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
        
        for i in range(len(arr)):
            arr[i]=arr[i][::-1]
        return arr


a = Solution()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = a.rotate_matrix(matrix)
for row in rotated:
    print(row)        

matrix2 = [
    [1, 2],
    [3, 4]
]

print(a.rotate_matrix(matrix2))                