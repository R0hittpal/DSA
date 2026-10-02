class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        longest=1
        hash=set(nums)
        for it in hash:
            if it-1 not in hash:
                count=1
                x=it
                while x+1 in hash:
                    x=x+1
                    count +=1
                longest=max(longest,count)
        return longest
            


