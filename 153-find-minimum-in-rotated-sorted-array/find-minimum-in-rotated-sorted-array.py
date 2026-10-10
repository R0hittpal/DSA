class Solution:
    def findMin(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        mini=float("inf")
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                if nums[mid]<mini:
                    mini=nums[mid]
                high=mid-1
            elif nums[mid]>=nums[low]:
            
                if nums[low]<mini:
                    mini=nums[low]
        
                low=mid+1
        return mini

            
        