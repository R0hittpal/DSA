class Solution:
    def fun(self,weight,mid):
        days=1 
        load=0
        for nums in weight:
            if load+nums>mid:
                days+=1
                load=nums
            else:
                load+=nums
        return days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        n=max(weights)
        high = sum(weights)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.fun(weights,mid)<=days:
                ans=mid
                high=mid-1

            else:
                low=mid+1
        return ans


        