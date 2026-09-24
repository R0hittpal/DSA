class Solution:
    def countKeyChanges(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(1,n):
           if s[i].lower() != s[i - 1].lower():
            count += 1

        return count