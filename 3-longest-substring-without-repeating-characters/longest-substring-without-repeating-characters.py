class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        maxi=0
        hash_map=set()
        while right<len(s):
            while s[right] in hash_map:
                hash_map.remove(s[left])
                left+=1
            hash_map.add(s[right])
            maxi=max(maxi,right-left+1)
            right+=1
        return  maxi

            