class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            result.append(count)
        j=0
        for i in range(len(nums)):
            nums[i]=result[j]
            j+=1
        return nums
        