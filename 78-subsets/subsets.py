class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        path=[]
        def sets(index):
            ans.append(path.copy())
            for i in range(index,len(nums)):
                path.append(nums[i])
                sets(i+1)
                path.pop()
        sets(0)
        return ans        
        