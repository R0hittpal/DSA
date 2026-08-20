class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list=dict()
        for i in nums:
            list[i]=list.get(i,0)+1
        
        for values in list.values():
            if values>1:
                return True
        
        return False
        
        