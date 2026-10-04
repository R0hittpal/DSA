class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high=len(nums)-1
        low=0
        while low <= high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                high=mid-1
            else:
                low=mid+1

        return -1
        