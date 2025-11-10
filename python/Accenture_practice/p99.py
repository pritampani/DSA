	# 	Set Matrix Zeroes

	# •	If element is 0, set its row & column to 0 in-place.


class Solution:
    def setmatrixzero(self,mat):
        isrow=False
        iscol=False

        for i in range(len(mat[0])):
            if mat[0][i]==0:
                isrow=True
        for i in range(len(mat)):
            if mat[i][0]==0:
                iscol=True
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                if mat[i][j]==0:
                    mat[0][j]=0
                    mat[i][0]=0
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
        if isrow:
            for i in range(len(mat[0])):
                mat[0][i]=0
        if iscol:
            for i in range(len(mat)):
                mat[i][0]=0
        return mat

            
a = Solution()

print(a.setmatrixzero([[1,1,1],[1,0,1],[1,1,1]]))


print(a.setmatrixzero([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))


print(a.setmatrixzero([[1,2,3],[4,5,6],[7,8,0]]))


print(a.setmatrixzero([[0,1],[2,3]]))
