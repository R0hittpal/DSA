class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i=0
        r=0
        n=len(nums)
        count=0
        maxi=0
        while r<n:
            if nums[r]==0:
                i=r+1
            count=r-i+1
            maxi=max(count,maxi)
            r+=1
        return maxi
        