class Solution:
    def fun1(self,nums,k):
        if k<0:
            return 0
        left=0
        n=len(nums)
        right=0
        count=0
        sumi=0
        while right<n:
            sumi+=(nums[right]%2)
            while sumi>k:
                sumi-=(nums[left]%2)
                left+=1
            count+=right-left+1
            right+=1
        return count
        

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        return self.fun1(nums,k)-self.fun1(nums,k-1)
        