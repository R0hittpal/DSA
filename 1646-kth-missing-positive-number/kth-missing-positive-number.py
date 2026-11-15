class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for nums in arr:
            if nums <=k:
                k+=1
            else:
                break
        return k
        