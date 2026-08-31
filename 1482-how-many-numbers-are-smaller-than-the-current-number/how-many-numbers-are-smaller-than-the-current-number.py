class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        snums=sorted(nums)
        dic={}
        for i ,num in enumerate(snums):
            if num not in dic:
                dic[num]=i
        for num in nums:
            result.append(dic[num])
        return result


        