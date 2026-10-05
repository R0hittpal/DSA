class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min=float("-inf")
        ind=0
        for i in range(len(nums)):
            if target in nums:
                if nums[i]==target:
                    return i
            else:
                if nums[i] >min and nums[i]<target:
                    min=nums[i]
                    ind=(nums.index(min))+1
        return ind


        