class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        left=0
        right=len(matrix[0])-1
        top=0
        bottam=len(matrix)-1
        while left<=right and top<=bottam:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            for i in range(top,bottam+1):
                result.append(matrix[i][right])
            right-=1

            if top <=bottam:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottam][i])
                bottam-=1
            if left<=right:
                for i in range(bottam,top-1,-1):
                    result.append(matrix[i][left]) 
                left+=1
        return result
        