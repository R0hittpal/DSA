class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        maxi = nums[0]

        for i in nums:
            total += i

            if total > maxi:
                maxi = total

            if total < 0:
                total = 0

        return maxi