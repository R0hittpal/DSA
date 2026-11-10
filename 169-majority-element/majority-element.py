class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        ele=0
        for i in range(len(nums)):
            if count==0:
                ele=nums[i]
                
            if nums[i]==ele:
                count+=1
            else:
                count-=1
        count1=0
        for i in nums:
            if i == ele:
                count1+=1
        n=len(nums)
        if count1>n/2:
            return ele  

        