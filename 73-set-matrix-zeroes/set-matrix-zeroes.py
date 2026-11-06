class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        first_row=False
        first_col=False
        for row in range(m):
            if matrix[row][0]==0:
                first_col=True
                break
        for col in range(n):
            if matrix[0][col]==0:
                first_row=True
                break
        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    matrix[0][col]=0


        for row in range(1,m):
            for col in range(1,n):
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0

        if first_row:
            for i in range(n):
                matrix[0][i]=0
        if first_col:
            for i in range(m):
                matrix[i][0]=0
        


        