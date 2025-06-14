#how to find determinant of a matrix

class Solution:
    def determinantOfMatrix(self, matrix, n):
        # Base case: if the matrix is 1x1, return the only element
        if n == 1:
            return matrix[0][0]

        det = 0  # Initialize the determinant

        # Loop through the first row of the matrix
        for i in range(n):
            # Calculate the cofactor by excluding the current row and column
            cofactor = self.getCofactor(matrix, 0, i, n)
            
            # Calculate the contribution to the determinant using Laplace expansion
            det += ((-1) ** i) * matrix[0][i] * self.determinantOfMatrix(cofactor, n - 1)

        return det

    def getCofactor(self, matrix, row, col, n):
        # Helper function to get the cofactor of a matrix
        cofactor = [[0] * (n - 1) for _ in range(n - 1)]
        i, j = 0, 0

        for row_idx in range(n):
            for col_idx in range(n):
                if row_idx != row and col_idx != col:
                    cofactor[i][j] = matrix[row_idx][col_idx]
                    j += 1
                    if j == n - 1:
                        j = 0
                        i += 1

        return cofactor
    
a = Solution()    
n = 4
matrix = [
    [1, 0, 2, -1],
    [3, 0, 0, 5],
    [2, 1, 4, -3],
    [1, 0, 5, 0]
]
print(a.determinantOfMatrix(matrix,n))