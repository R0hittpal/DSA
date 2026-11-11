class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros=0
        right=0
        left=0
        maxi=0
        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            if zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        