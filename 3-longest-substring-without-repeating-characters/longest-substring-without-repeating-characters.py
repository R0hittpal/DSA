class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        for i  in range(len(s)):
            hashi={}
            for j in range(i,len(s)):
                if hashi.get(s[j], 0) == 1:
                    break

                length=j-i+1
                max_len=max(length,max_len)
                hashi[s[j]]=1
        return max_len
        