class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        largest=float('-inf')
        for i in accounts:
            sum=0
            for j in i:
                sum=j+sum
            if sum > largest:
                largest=sum

        return largest