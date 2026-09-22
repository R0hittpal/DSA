class Solution:
    def generaterow(self,n):
        ans=[]
        res=1
        ans.append(1)
        for i in range(1,n):
            res=res*(n-i)
            res=res//i
            ans.append(res)
        return ans


    def generate(self, numRows: int) -> list[list[int]]:
        ans=[]
        for i in range(1,numRows+1):
            ans.append(self.generaterow(i))
        return ans


        