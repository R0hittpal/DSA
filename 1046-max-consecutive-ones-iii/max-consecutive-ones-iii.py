class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left,right=0,0
        n=len(nums)
        zeros=0
        maxi=0
        while right<n:
            if nums[right]==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            length=right-left+1
            maxi=max(maxi,length)
            right +=1
        
        return maxi
