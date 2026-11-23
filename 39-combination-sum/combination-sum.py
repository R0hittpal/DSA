class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        def fun(arr,path,index,sumi):
            if sumi == target:
                ans.append(path.copy())
                return
            if index == len(arr) or sumi > target:
                return
            path.append(arr[index])
            fun(arr,path,index,sumi+arr[index])
            path.pop()
            fun(arr,path,index+1,sumi)
        fun(candidates,[],0,0)
        return ans


        