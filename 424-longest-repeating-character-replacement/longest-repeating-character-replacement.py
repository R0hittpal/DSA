class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r=0
        l=0
        max_len=0
        max_f=0
        freq={}
        while r<len(s):
            freq[s[r]]=freq.get(s[r],0)+1
            max_f=max(max_f,freq[s[r]])
            while (r - l + 1) - max_f>k:
                freq[s[l]]-=1
                
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len

        
        
        