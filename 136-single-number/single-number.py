class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            map[i]=map.get(i,0)+1
        for key,value in map.items():
            if value==1:
                return key
        
        