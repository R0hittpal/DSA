class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        map={}
        for i in sentence:
            map[i]=map.get(i,0)+1
        return len(map)==26