class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer=[]
        current=[]
        def backtrack(index, remaining_target):
            if remaining_target==0:
                answer.append(current.copy())
                return
            if index == len(candidates):
                return
            # If current candidate can fit into remaining target, pick it.
            if candidates[index] <= remaining_target:
                current.append(candidates[index])
 
                # Stay at same index because the same candidate can be reused.
                backtrack(index, remaining_target - candidates[index])
 
                # Remove last picked element before trying another possibility.
                current.pop()
            else:
                # If candidate is greater than remaining target, it cannot be picked.
                pass
 
            # Skip current candidate and move to the next index.
            backtrack(index + 1, remaining_target)
 
        # Start exploring combinations from index 0.
        backtrack(0, target)
 
        return answer
 