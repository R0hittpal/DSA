class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        n=len(s)
        maxi=0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            length=i-left+1
            maxi=max(maxi,length)
        return maxi


       