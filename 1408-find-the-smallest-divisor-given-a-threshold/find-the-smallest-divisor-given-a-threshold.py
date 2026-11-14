class Solution:
    def sum_mid(self,nums,mid):
        total=0
        n=len(nums)
        for i in range(n):
            total+=(nums[i]+mid-1)//mid
        return total
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.sum_mid(nums,mid)<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
