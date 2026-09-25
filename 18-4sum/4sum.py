class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans=set()
        n=len(nums)
        for i in range(n-2):
            
            for j in range(i+1,n-1):
                seen=set()
                for k in range(j+1,n):
                    composite=target-(nums[i]+nums[j]+nums[k])
                    if composite in seen:
                        ans.add(tuple(sorted([nums[i],nums[j],nums[k],composite])))
                    seen.add(nums[k])
        return [list(x) for x in ans]

        