class Solution:
    def firstUniqChar(self, s: str) -> int:
        map={}
        c=0
        for i in s:
            map[i]=map.get(i,0)+1
        for key,values in map.items():
            if values==1:
                c=key
                break
        for i in range(len(s)):
            if s[i] ==c:
                return i
        return -1



            
        