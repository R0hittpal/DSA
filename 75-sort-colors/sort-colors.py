class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros=0
        ones=0
        twos=0

        for i in nums:
    
            if i==0:
                zeros+=1
            elif i==1:
                ones+=1
            else:
                twos+=1
        j=0
        while j<len(nums):
            while j<zeros:
                nums[j]=0
                j+=1
            while j<zeros+ones:
                nums[j]=1
                j+=1
            while j<len(nums):
                nums[j]=2
                j+=1
            return nums
    
    