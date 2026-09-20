class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        f_row=False
        f_col=False

        for i in range(n):
            if matrix[0][i]==0:
                f_row=True
                break 
        for j in range(m):
            if matrix[j][0]==0:
                f_col=True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0 :
                    matrix[i][j]=0
        
        if f_row ==True:
        
            for i in range(n):
            
                matrix[0][i]=0
        if f_col == True:    
            for j in range(m):
            
                matrix[j][0]=0

        
    



