class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        index=-1
        value=0
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index=i
                break
        if index==-1:
            nums.reverse()
            return
        for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                value=i
                break
        nums[value],nums[index]=nums[index],nums[value]

        nums[index+1:]=reversed(nums[index+1:])
