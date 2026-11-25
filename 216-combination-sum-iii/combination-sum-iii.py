class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans=[]
        current=[]
        def backtrack(index,current,target):
            if len(current)==k:
                if target==0:
                    ans.append(current.copy())
                return
            for i in range(index,10):
                if i>target:
                    break
                current.append(i)
                backtrack(i + 1, current, target - i)
                current.pop()

        backtrack(1,current,n)
        return ans
