class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lst=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i] >=0:
                lst[p]=nums[i]
                p+=2
            if nums[i]<0:
                lst[n]=nums[i]
                n+=2
        return lst
        