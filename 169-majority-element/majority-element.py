class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=1
        ele=nums[0]
        for i in nums:
            if i==ele:
                count+=1
            elif i!=ele:
                count-=1
            if count==0:
                ele =i
                count=1
        count1=0
        for i in nums:
            if ele==i:
                count1+=1
        if count1> len(nums)//2:
            return ele
        else:
            return -1

        