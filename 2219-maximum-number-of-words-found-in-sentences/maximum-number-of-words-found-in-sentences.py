class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for i in sentences:
            count=0
            i=i.split()
            for j in i:
                count+=1
            maxi=max(count,maxi)
        return maxi
        