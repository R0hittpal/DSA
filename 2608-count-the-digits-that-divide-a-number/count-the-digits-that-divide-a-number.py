class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        org=num
        while num >0:
            digit=num%10
            if org%digit==0:
                count+=1
            num=num//10
        return count            

        