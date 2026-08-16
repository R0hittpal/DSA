class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max=float("-inf")
        sec=float("-inf")
        third=float("-inf")
        for i in nums:
            if i>max:
                third=sec
                sec=max
                max=i
            elif i>sec and i <max:
                third=sec
                sec=i 
            elif i>third and i <sec:
                third=i
        if len(nums)==2 or third==float("-inf") :
            third=max

                
            
        return third      