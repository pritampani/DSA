# Matrix Spiral Print – Print all elements of a matrix in spiral order.
# Description: Traverse the matrix layer by layer.
# Sample I/O:
# Input: [[1,2,3],[4,5,6],[7,8,9]] → Output: 1 2 3 6 9 8 7 4 5.
# Topic: Matrix / Loops. Difficulty: Medium. (Popular pattern)



class Solution:
    def sprial_matrix(self,mat):
        if not mat:
            return []

        res=[]
        top=0
        bottom=len(mat)-1
        left=0
        right=len(mat[0])-1

        while top<=bottom and left<=right:
            for j in range(left,right+1):
                res.append(mat[top][j])
            top+=1
            for i in range(top,bottom+1):
                res.append(mat[i][right])
            right-=1

            if top<=bottom:
                for j in range(right,left-1,-1):
                    res.append(mat[bottom][j])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left])
                left+=1
        return res
    

a = Solution()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(a.sprial_matrix(matrix))  # Expected: [1,2,3,6,9,8,7,4,5]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(a.sprial_matrix(matrix2)) # Expected: [1,2,3,4,8,12,11,10,9,5,6,7]