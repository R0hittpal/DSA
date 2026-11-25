class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        path=[]
        def backtrack(index):
            ans.append(path.copy())
            for i in range(index,len(nums)):

                if i>index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans
        