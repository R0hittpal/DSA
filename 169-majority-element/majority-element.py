class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        a=len(nums)
        for i in range(len(nums)):
            dict[nums[i]]=dict.get(nums[i],0)+1
        for key in dict:
            if dict[key] > a / 2:
                return key
       