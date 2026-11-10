class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=0
        neg=1
        n=len(nums)
        ans=[0]*n
        for i in range(len(nums)):
            if nums[i]>=0:
                ans[pos]=nums[i]
                pos+=2
            elif nums[i]<0:
                ans[neg]=nums[i]
                neg+=2
        return ans


        