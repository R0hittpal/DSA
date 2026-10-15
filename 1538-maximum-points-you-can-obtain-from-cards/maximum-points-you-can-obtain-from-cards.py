class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left_sum=sum(cardPoints[0:k])
        right_sum=0
        left=k-1
        n=len(cardPoints)
        right=n-1
        total=0
        maxi=left_sum
        while left>=0 :
            left_sum-=cardPoints[left]
            right_sum+=cardPoints[right]
            total=left_sum +right_sum
            maxi=max(maxi,total)
            left-=1
            right-=1

        return maxi
