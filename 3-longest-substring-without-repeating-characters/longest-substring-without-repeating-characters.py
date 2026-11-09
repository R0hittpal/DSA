class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        hashi=set()
        n=len(s)
        maxi=0
        for right in range(n):
            while s[right] in hashi:
                hashi.remove(s[left])
                left+=1
            hashi.add(s[right])
            length=right-left+1
            maxi=max(length,maxi)
        return maxi
            

        