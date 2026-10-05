class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        index=len(nums)
        while low<=high:
            mid=(high+low)//2
            if nums[mid] >= target:
                index=mid
                high=mid-1
            else:
                low=mid+1
        return index

        