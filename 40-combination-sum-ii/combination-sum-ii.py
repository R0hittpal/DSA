class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans=[]
        current=[]
        def backtrack(index,current,target):
            if target==0:
                ans.append(current.copy())
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break

                current.append(candidates[i])
                backtrack(i+1,current,target-candidates[i])
                current.pop()
        backtrack(0,current,target)
        return ans


        