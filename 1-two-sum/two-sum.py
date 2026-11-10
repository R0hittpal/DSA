class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in seen:
                return [i,seen[com]]
            seen[nums[i]]=i
        