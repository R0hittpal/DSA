class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict ={}
        for i in range(len(numbers)):
            com=target-numbers[i]
            if com in dict:
                return [dict[com]+1,i+1]
            dict[numbers[i]]=i
        