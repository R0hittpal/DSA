class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def para(open,close,path):
            if len(path)==2*n:
                ans.append(path)
                return
            if open<n:
                para(open+1,close,path+"(")
            if close<open:
                para(open,close+1,path+")")
        para(0,0,"")
        return ans
        