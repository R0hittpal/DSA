class Solution:
    def fun1(self,nums,goal):
        if goal<0:
            return 0
        left=0
        n=len(nums)
        count=0
        right=0
        sumi=0
        while right<n:
            sumi+=nums[right]
            while left<=right and sumi>goal:
                sumi-=nums[left]
                left+=1
            count+=right-left+1
            right+=1
        return count
        

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        return self.fun1(nums,goal)-self.fun1(nums,goal-1)
    