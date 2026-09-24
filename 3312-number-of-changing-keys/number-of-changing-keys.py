class Solution:
    def countKeyChanges(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(1,n):
           if s[i].isupper():
            if s[i] != s[i-1].upper():
                count+=1
           if s[i].islower():
            if s[i] != s[i-1].lower():
                count+=1
        return count