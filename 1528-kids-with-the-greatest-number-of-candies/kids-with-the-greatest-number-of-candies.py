class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=float('-inf')
        for i in candies:
            if i > maxi:
                maxi=i
        list=[]
        for i in candies:
            list.append(i+extraCandies>=maxi)
        return list