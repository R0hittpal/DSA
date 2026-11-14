class Solution:
    def sum_mid(self,nums,mid):
        total=0
        n=len(nums)
        for i in range(n):
            total+=(nums[i]+mid-1)//mid
        return total
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.sum_mid(piles,mid)<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        