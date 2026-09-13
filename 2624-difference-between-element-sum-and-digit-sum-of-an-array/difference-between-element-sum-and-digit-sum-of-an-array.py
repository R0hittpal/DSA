class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elesum=0
        digitsum=0
        for i in nums:
            elesum+=i
            while i>0:
                digit=i%10
                digitsum+=digit
                i=i//10
        return elesum-digitsum
        