class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans=[]
        ans.append(1)
        res=1
        for i in range(1,rowIndex+1):
            res=res*(rowIndex+1-i)
            res=res//i
            ans.append(res)
        return ans