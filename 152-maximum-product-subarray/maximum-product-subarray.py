class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        pre=1
        sur=1
        n=len(nums)
        maxi=float("-inf")
        for i in range(n):
            
            if pre==0:
                pre=1
            if sur==0:
                sur=1
            pre=pre*nums[i]
            sur=sur*nums[n-i-1]
            maxi=max(maxi,max(pre,sur))
        return maxi

        